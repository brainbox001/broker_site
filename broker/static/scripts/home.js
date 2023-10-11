
window.addEventListener('scroll', revealLine)

function revealLine(){
  const revealLines = document.querySelectorAll('.line-reveal')
  for(let i = 0; i < revealLines.length; i++){
    const windowHeight = window.innerHeight;
    const revealTop = revealLines[i].getBoundingClientRect().top;
    const revealPoint = 250;

    if (revealTop < windowHeight - revealPoint){
      revealLines[i].classList.add('active-line')
    }else{revealLines[i].classList.remove('active-line')}
  }
}

window.addEventListener('scroll', revealDiv)

function revealDiv(){
  const revealDivs = document.querySelectorAll('.div-reveal')
  for(let i = 0; i < revealDivs.length; i++){
    const windowHeight = window.innerHeight;
    const revealTop = revealDivs[i].getBoundingClientRect().top;
    const revealPoint = 200;

    if (revealTop < windowHeight - revealPoint){
      revealDivs[i].classList.add('active-div')
    }else{revealDivs[i].classList.remove('active-div')}
  }
}


const showTitles = document.querySelectorAll('.title-show');
const navbarHead = document.querySelector('.navbar-head');

function checkVisibility() {
  let isVisible = false;

  for (let i = 0; i < showTitles.length; i++) {
    const windowHeight = window.innerHeight;
    const revealTop = showTitles[i].getBoundingClientRect().top;
    const revealBottom = showTitles[i].getBoundingClientRect().bottom;


    if (revealTop < windowHeight && revealBottom > 0) {
      const innerHTML = showTitles[i].innerHTML;
      navbarHead.innerHTML = innerHTML; 
      document.getElementById("navbar").style.top = "0";
      isVisible = true; 
      break;
    }
  }


  if (window.scrollY === 0) {
    isVisible = false
    navbarHead.innerHTML = '';
    document.getElementById("navbar").style.top = "-150px";
  }
}


checkVisibility();


window.addEventListener('scroll', checkVisibility);
