document.addEventListener("DOMContentLoaded", function () {
  
  const checkmark = document.getElementById("_id_checkmark");
  const checkbox = document.getElementById("termsCheckbox");
  const submitButton = document.getElementById("submitButton");

  checkmark.addEventListener("click", function () {
      checkbox.checked = !checkbox.checked; 
      
      if (checkbox.checked) {
          submitButton.removeAttribute("disabled");
      } else {
          submitButton.setAttribute("disabled", "disabled");
      }
  });
});