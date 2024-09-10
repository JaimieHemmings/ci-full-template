document.addEventListener('DOMContentLoaded', function() {

  // Toggle Menu Icon
  const navButton = document.getElementById('menu-toggle');
  const menu = document.getElementById('menu-container');
  navButton.addEventListener(
    'click',()=>{
      menu.classList.toggle('hidden');
      navButton.classList.toggle('active');
    }
  );

  // get all instances of hover-pop class
  const hoverPop = document.querySelectorAll('.hover-pop');
  
  // if there are instances of hover-pop
  if(hoverPop) {
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
    
    // Every second animate a random letter
    const letters = document.querySelectorAll('.letter');
    setInterval(() => {
      letters.forEach((letter) => {
        letter.classList.remove('hover');
      });
      let random = Math.floor(Math.random() * letters.length);
      letters[random].classList.toggle('hover');
    }, 1000);
  }

  // Toggle FAQ answers
  const faqItems = document.querySelectorAll('.faq-item');
  // if there are instances of faq
  if(faqItems) {
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
  }

  
  // Mission Statement Generator
  const missionStatement = document.getElementById('mission-statement');
  const btnMissionGenerator = document.getElementById('btn-mission-generator');

  function numberGenerator() {
   return Math.floor(Math.random() * mission_statements.length);
  }
    
  // if there is a mission statement and a button
  if (btnMissionGenerator) {
    btnMissionGenerator.addEventListener('click', () => {
      missionStatement.innerText = mission_statements[numberGenerator()];
    });
  }
});

// Mission Statement bank
const mission_statements = [
  "Our mission is to create digital waves that have an impact. We believe that the best way to do this is by creating custom software that helps businesses grow and succeed. We take the time to understand your business and your goals so that we can create software that helps you achieve them.",
  "Empowering businesses through innovative, scalable web applications that drive growth and deliver exceptional user experiences.",
  "To craft high-performance web applications that seamlessly integrate with our clients’ vision, propelling their digital transformation.",
  "Transforming ideas into powerful web solutions, ensuring our clients stay ahead in the digital landscape with cutting-edge technology.",
  "Building robust, secure, and user-friendly web applications that enhance operational efficiency and customer engagement.",
  "To lead the web development industry by delivering custom, future-ready applications that exceed client expectations and fuel business success.",
  "Designing and developing web applications that simplify complexity, enabling our clients to focus on their core business objectives.",
  "To be the trusted partner in web development, delivering intuitive, scalable solutions that help businesses thrive in a connected world.",
  "Creating bespoke web applications that not only meet industry standards but set new benchmarks for innovation and user satisfaction.",
  "Empowering our clients with state-of-the-art web applications that foster growth, efficiency, and a competitive edge in the market.",
  "To deliver transformative web applications that blend creativity and technology, providing businesses with a seamless digital experience."
];