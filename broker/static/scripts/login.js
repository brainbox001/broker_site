const loader = document.getElementById('loader');
loader.style.display = 'block';
document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");
  
  loader.style.display = 'none';

  loginForm.addEventListener('submit', function (e) {
   
    e.preventDefault();

    loader.style.display = 'block';
    const formData = new FormData(loginForm);
    
    const xhr = new XMLHttpRequest();

    xhr.open('POST', '/login', true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.success) {
                window.location.href = '/dashboard'; 
            } else {
                document.getElementById('errorcode').textContent = response.message; 
            }
        } else {
            // Handle other HTTP status codes if needed
        }
        loader.style.display = 'none';
    };

    xhr.send(formData);
     
  
  });

});