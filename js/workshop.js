/* Copy the visible code, not a second hidden copy. No analytics or data uploads. */
(function(){
  'use strict';
  const timers = new WeakMap();
  const t = text => window.WorkshopPreferences?.t(text) || text;
  function announce(text){
    let status=document.getElementById('copy-status');
    if(!status){status=document.createElement('div');status.id='copy-status';status.setAttribute('role','status');document.body.append(status);}
    status.textContent=text;setTimeout(()=>{if(status.textContent===text)status.textContent='';},2200);
  }
  async function copyText(text){
    try{if(!navigator.clipboard)throw new Error('No clipboard API');await navigator.clipboard.writeText(text);return true;}
    catch(error){
      const area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.cssText='position:fixed;top:-1000px';document.body.append(area);area.select();
      let ok=false;try{ok=document.execCommand('copy');}catch(e){ok=false;}area.remove();return ok;
    }
  }
  function state(box){
    if(!timers.has(box))timers.set(box,{remaining:Number(box.dataset.seconds)*1000,end:0,running:false});
    return timers.get(box);
  }
  function draw(box){
    const timer=state(box);if(timer.running){timer.remaining=Math.max(0,timer.end-Date.now());if(!timer.remaining)timer.running=false;}
    const seconds=Math.ceil(timer.remaining/1000);
    const time=String(Math.floor(seconds/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0');
    const output=box.querySelector('output'),button=box.querySelector('[data-timer="toggle"]');
    if(output.textContent!==time)output.textContent=time;
    const label=t(timer.running?'Pause':seconds===0?'Restart':'Start');
    if(button.textContent!==label)button.textContent=label;
    box.classList.toggle('finished',seconds===0);
  }
  function closeVideos(){document.querySelectorAll('.video-stage iframe').forEach(frame=>{delete frame.parentElement.dataset.loaded;frame.remove();});}
  document.addEventListener('click',async event=>{
    const copy=event.target.closest('button.copy');
    if(copy){
      const code=copy.closest('.prompt')?.querySelector('pre code, pre');
      if(!code){announce(t('No prompt found.'));return;}
      const ok=await copyText(code.textContent);announce(t(ok?'Prompt copied.':'Copy unavailable: select and copy the prompt text.'));
      copy.textContent=t(ok?'Copied':'Select text to copy');setTimeout(()=>copy.textContent=t('Copy prompt'),1500);return;
    }
    const timer=event.target.closest('[data-timer]');
    if(timer){const box=timer.closest('.timer'),value=state(box);if(timer.dataset.timer==='reset'){value.running=false;value.remaining=Number(box.dataset.seconds)*1000;}else if(value.running){value.remaining=Math.max(0,value.end-Date.now());value.running=false;}else{if(!value.remaining)value.remaining=Number(box.dataset.seconds)*1000;value.end=Date.now()+value.remaining;value.running=true;}draw(box);return;}
    const play=event.target.closest('.play-clip');
    if(play){
      const box=play.closest('[data-video]');closeVideos();const frame=document.createElement('iframe');
      const query=new URLSearchParams({start:box.dataset.start,end:box.dataset.end,autoplay:'1',rel:'0',playsinline:'1',enablejsapi:'1',origin:location.origin});
      frame.src='https://www.youtube-nocookie.com/embed/'+box.dataset.video+'?'+query;frame.title=box.querySelector('p').textContent+' excerpt';frame.allow='autoplay; encrypted-media; picture-in-picture';frame.allowFullscreen=true;frame.referrerPolicy='strict-origin-when-cross-origin';box.dataset.loaded='true';box.append(frame);return;
    }
    if(event.target.closest('[data-notes]'))window.Reveal?.getPlugin('notes')?.open();
  });
  setInterval(()=>document.querySelectorAll('.timer').forEach(draw),250);
  document.addEventListener('workshoplanguagechange',()=>document.querySelectorAll('.timer').forEach(draw));
  window.initWorkshop=function(){if(window.Reveal){Reveal.on('slidechanged',closeVideos);Reveal.on('overviewshown',closeVideos);}};
  document.addEventListener('visibilitychange',()=>{if(document.hidden)document.querySelectorAll('.video-stage iframe').forEach(f=>f.contentWindow?.postMessage(JSON.stringify({event:'command',func:'pauseVideo',args:[]}), 'https://www.youtube-nocookie.com'));});
})();
