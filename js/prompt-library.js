/* Both languages share stable IDs, filter values and the same open <details>. */
(function () {
  'use strict';
  const library = document.getElementById('library'), search = document.getElementById('search');
  const category = document.getElementById('category'), mode = document.getElementById('mode');
  const count = document.getElementById('count');
  const prefs = () => window.WorkshopPreferences;
  const zh = () => prefs()?.language === 'zh';
  const labels = { Understand:'理解概念', Materials:'课程材料', Recall:'回忆自测', Reasoning:'推理解题', Feedback:'反馈修改', Verification:'核查来源', Planning:'学习规划', Explore:'互动探索', Explain:'讲解', Practice:'练习', Any:'不限' };
  const stableValues = Object.fromEntries(Object.entries(labels).map(([key, value]) => [value, key]));
  const records = [];
  library.dataset.noTranslate = ''; count.dataset.noTranslate = '';
  function parse(text, chinese) {
    const keys = chinese ? ['类别','模式','适用场景','填写内容','核查要点'] : ['Category','Mode','Use for','Fill in','Check'];
    return text.split(/^## /m).slice(1).map(chunk => {
      const title = chunk.split('\n')[0].trim(), id = title.match(/^\d+/)?.[0];
      const code = chunk.match(/```text\r?\n([\s\S]*?)\r?\n```/)?.[1];
      const values = keys.map(key => chunk.match(new RegExp('^' + key + ': (.+)$', 'm'))?.[1]);
      if (!id || !code || values.some(value => !value)) throw new Error('Incomplete prompt translation');
      return { id, title, code, category:stableValues[values[0]] || values[0], mode:stableValues[values[1]] || values[1], meta:values.slice(2), search:chunk.toLowerCase() };
    });
  }
  function filter() {
    let visible = 0;
    const query = search.value.trim().toLowerCase();
    records.forEach(r => {
      const matches = (!query || r.search.includes(query)) && (!category.value || r.en.category === category.value) && (!mode.value || r.en.mode === mode.value);
      r.el.hidden = !matches; if (matches) visible++;
    });
    count.textContent = zh() ? `显示 ${visible} / ${records.length} 个模板` : `${visible} of ${records.length} templates`;
  }
  function render() {
    records.forEach(r => {
      const data = zh() ? r.zh : r.en;
      r.summary.textContent = data.title;
      r.meta.forEach((p, i) => {
        p.firstChild.textContent = (zh() ? ['适用场景','填写内容','核查要点'] : ['Use for','Fill in','Check'])[i] + (zh() ? '：' : ': ');
        p.lastChild.textContent = data.meta[i];
      });
      r.tag.textContent = zh() ? labels[data.category] + ' · ' + labels[data.mode] : data.category + ' · ' + data.mode;
      r.code.textContent = data.code;
      r.button.textContent = zh() ? '复制提示词' : 'Copy prompt';
    });
    for (const option of category.options) if (option.value) option.textContent = zh() ? labels[option.value] : option.value;
    filter();
  }
  function openHash() {
    const record = records.find(r => r.el.id === location.hash.slice(1));
    if (record) { search.value=''; category.value=''; mode.value=''; filter(); record.el.open=true; record.el.scrollIntoView({block:'start'}); }
  }
  async function load() {
    try {
      const texts = await Promise.all(['undergraduate-study-prompts.md','undergraduate-study-prompts.zh.md'].map(async file => {
        const response = await fetch(file); if (!response.ok) throw new Error('Prompt source unavailable'); return response.text();
      }));
      const english = parse(texts[0], false), chinese = new Map(parse(texts[1], true).map(r => [r.id, r]));
      if (english.length !== 20 || chinese.size !== english.length) throw new Error('Prompt count mismatch');
      for (const en of english) {
        const translated = chinese.get(en.id);
        if (!translated || en.category !== translated.category || en.mode !== translated.mode) throw new Error('Prompt metadata mismatch');
        const el = document.createElement('details'); el.className='box'; el.id='prompt-'+en.id;
        const summary = document.createElement('summary'); el.append(summary);
        const meta = Array.from({length:3}, () => { const p=document.createElement('p');p.append(document.createElement('strong'),document.createTextNode(''));el.append(p);return p; });
        const tag=document.createElement('p');tag.className='hint';el.append(tag);
        const wrapper=document.createElement('div');wrapper.className='prompt';
        const pre=document.createElement('pre'),code=document.createElement('code'),button=document.createElement('button');
        pre.append(code);button.type='button';button.className='copy';wrapper.append(pre,button);el.append(wrapper);
        library.append(el);
        records.push({en,zh:translated,el,summary,meta,tag,code,button,search:en.search+'\n'+translated.search+'\n'+labels[en.category]});
      }
      Array.from(new Set(english.map(r=>r.category))).sort().forEach(value=>{const option=document.createElement('option');option.value=value;option.textContent=value;category.append(option);});
      render();openHash();library.dataset.ready='true';
    } catch (error) {
      count.textContent = zh() ? '模板加载失败，请打开上方的 Markdown 原文。' : 'Could not load templates. Open the Markdown source link above.';
      library.dataset.error='true';
    }
  }
  search.addEventListener('input',filter);category.addEventListener('change',filter);mode.addEventListener('change',filter);
  document.addEventListener('workshoplanguagechange',render);window.addEventListener('hashchange',openHash);
  load();
})();
