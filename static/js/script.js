const btnHamburger = document.querySelector('#btnHamburger');
const rightMenu = document.querySelector('#rightMenu');

btnHamburger.addEventListener('click', function (){
  console.log('click hamburger');

  if(rightMenu.classList.contains('close')){
    rightMenu.classList.remove('close');
    console.log('open hamburger');
  } else {
    rightMenu.classList.add('close');
    console.log('close hamburger');
  }
});
