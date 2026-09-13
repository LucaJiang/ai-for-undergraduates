document.addEventListener('click', async (event) => {
  const button = event.target.closest('[data-copy]');
  if (!button) return;
  try {
    await navigator.clipboard.writeText(button.dataset.copy);
    const oldText = button.textContent;
    button.textContent = 'Copied';
    button.classList.add('copied');
    window.setTimeout(() => {
      button.textContent = oldText;
      button.classList.remove('copied');
    }, 1400);
  } catch (error) {
    button.textContent = 'Copy failed';
  }
});
