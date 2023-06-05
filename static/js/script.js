const btnHamburger = document.querySelector('#btnHamburger');
const menu = document.querySelector('#menu');
const span1 = document.getElementById('span1');
const span2 = document.getElementById('span2');
const span3 = document.getElementById('span3');


btnHamburger.addEventListener('click', () => {
  console.log('click hamburger');

  if(menu.classList.contains('hidden')){ // Open Hamburger Menu Toggle
    menu.classList.remove('hidden');
    span1.classList.add('open-span1');
    span2.classList.add('open-span2');
    span3.classList.add('open-span3');
    console.log('open hamburger');
  } else {
    menu.classList.add('hidden');
    span1.classList.remove('open-span1');
    span2.classList.remove('open-span2');
    span3.classList.remove('open-span3');
    console.log('close hamburger');
  }
});
