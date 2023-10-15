document.addEventListener("DOMContentLoaded", function () {
  
  const checkmark = document.getElementById("_id_checkmark");
  const checkbox = document.getElementById("termsCheckbox");
  const registerForm = document.getElementById("registerForm");
  const loader = document.getElementById('loader');

  checkmark.addEventListener("click", function () {
      checkbox.checked = !checkbox.checked; 
      
      if (checkbox.checked) {
          submitButton.removeAttribute("disabled");
      } else {
          submitButton.setAttribute("disabled", "disabled");
      }
  });

  registerForm.addEventListener('submit', function (e) {
   
    e.preventDefault();

    loader.style.display = 'block';

    const formData = new FormData(registerForm);

    const errorElements = document.querySelectorAll('.errorlist');
    errorElements.forEach(errorElement => errorElement.remove());

    fetch('/sign-up', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        
        if (data.success) {

            window.location.href = '/verify_email/';
        } else {
            if (data.not_found) {
                document.getElementById('errorCode').textContent = data.not_found;
            } else if (data.error_message) {
                document.getElementById('errorCode').textContent = data.error_message;
            } else{
                for (const field in data.errors) {
                    const error = data.errors[field];
                    const element = document.getElementById(`id_${field}`);
                
                    if (element) {
                
                        element.className = 'error-edit';
                        const errorElement = document.createElement('div');
                        
                        errorElement.className = 'errorlist';
                        errorElement.textContent = error;
                        element.parentNode.insertBefore(errorElement, element.nextSibling);
                        
            }
        }
           
            }
              
        }

    })
        .catch(error => {
            if (error.name === 'SyntaxError' || error.message.includes('Unexpected token')) {
                
                document.getElementById('errorCode').textContent = "Can't parse empty form";
            } else {
                
                console.error('Error:', error);
            }
    })

        .finally(() => {

            loader.style.display = 'none';
        })
        }) 
  
});
