document.getElementById('faq-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const q = this.question.value;
  const a = this.answer.value;
  const res = await fetch('http://localhost:8000/faqs/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({question: q, answer: a})
  });
  loadFaqs();
});

async function loadFaqs() {
  const res = await fetch('http://localhost:8000/faqs/');
  const faqs = await res.json();
  const list = document.getElementById('faqs-list');
  list.innerHTML = faqs.map(faq => `<div><b>${faq.question}</b><br>${faq.answer}</div>`).join('');
}

document.getElementById('tip-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const t = this.tip.value;
  const c = this.created_by.value;
  await fetch('http://localhost:8000/healthtips/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({tip: t, created_by: c})
  });
  loadTips();
});

async function loadTips() {
  const res = await fetch('http://localhost:8000/healthtips/');
  const tips = await res.json();
  const list = document.getElementById('tips-list');
  list.innerHTML = tips.map(tip => `<div>${tip.tip} <i>(${tip.created_by})</i></div>`).join('');
}

window.onload = function() {
  loadFaqs();
  loadTips();
}
