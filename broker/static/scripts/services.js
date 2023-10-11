window.addEventListener('scroll', revealLine)

function revealLine(){
  const revealLines = document.querySelectorAll('.line-reveal')
  for(let i = 0; i < revealLines.length; i++){
    const windowHeight = window.innerHeight;
    const revealTop = revealLines[i].getBoundingClientRect().top;
    const revealBottom = revealLines[i].getBoundingClientRect().bottom;

    if (revealTop < windowHeight && revealBottom > 0) {
      revealLines[i].classList.add('active-line')
    }else{revealLines[i].classList.remove('active-line')}
  }
}