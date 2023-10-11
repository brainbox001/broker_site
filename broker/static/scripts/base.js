function myFunction() {
  let x = document.getElementById("listed-menu");

  if (x.className === "nav-menu") {
    x.className += " responsive";
    
  } else {
    x.className = "nav-menu";
  }
}
