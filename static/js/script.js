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

});