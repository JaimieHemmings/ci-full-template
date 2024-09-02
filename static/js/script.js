document.addEventListener('DOMContentLoaded', function() {

  // get all instances of hover-pop class
  const hoverPop = document.querySelectorAll('.hover-pop');
  // split each letter of each instance of hover-pop
  hoverPop.forEach((el) => {
    let text = el.innerText;
    let splitText = text.split('');
    el.innerText = '';
    splitText.forEach((letter) => {
      let span = document.createElement('span');
      span.classList.add('letter');
      span.innerText = letter;
      el.appendChild(span);
    });
  });

  // Toggle Menu Icon
  const navButton = document.getElementById('menu-toggle');
  const menu = document.getElementById('menu-container');
  navButton.addEventListener(
    'click',()=>{
      menu.classList.toggle('hidden');
      navButton.classList.toggle('active');
    }
  );

  // Toggle FAQ answers

  const faq = document.getElementById('faq-list');

  faqItems = faq.querySelectorAll('.faq-item');

  faqItems.forEach((item) => {
    item.addEventListener('click', () => {
      faqItems.forEach((faqItem) => {
        if (faqItem !== item) {
          faqItem.classList.remove('active');
        }
      });
      item.classList.toggle('active');
    });
  });
});