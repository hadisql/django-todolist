const btnHamburger = document.querySelector('#btnHamburger');
const menu = document.querySelector('#menu');
const span1 = document.getElementById('span1');
const span2 = document.getElementById('span2');
const span3 = document.getElementById('span3');

const deleteButton = document.getElementById('delete_button');
const deleteYesButton = document.getElementById('delete_yes');
const deleteNoButton = document.getElementById('delete_no');
const deleteMessage = document.getElementById('delete_message')



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


deleteButton.addEventListener('click', () => {
  console.log('deleted Task -> show delete confirmation');

  deleteButton.classList.add('hidden');
  deleteNoButton.classList.remove('hidden');
  deleteYesButton.classList.remove('hidden');
  deleteMessage.classList.remove('hidden');
})

deleteNoButton.addEventListener('click', () => {
  console.log('task NOT deleted');

  deleteButton.classList.remove('hidden');
  deleteNoButton.classList.add('hidden');
  deleteYesButton.classList.add('hidden');
  deleteMessage.classList.add('hidden');
})
