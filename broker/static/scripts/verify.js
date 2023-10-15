
  document.addEventListener('DOMContentLoaded', function () {
    const verifyForm = document.getElementById('verify-form');
  
    const errorMessage = document.getElementById('error-message');
    const loader = document.getElementById('loader');


    verifyForm.addEventListener('submit', function (e) {
        e.preventDefault();
        
        loader.style.display = 'block';
        const formData = new FormData(verifyForm);
        
        const xhr = new XMLHttpRequest();

        xhr.open('POST', '/verify_email/', true);

        xhr.onload = function () {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                if (response.success) {
                    window.location.href = '/dashboard'; 
                } else {
                    document.getElementById('error-message').textContent = response.message; 
                }
            } else {
                // Handle other HTTP status codes if needed
            }
            loader.style.display = 'none';
        };

        xhr.send(formData);
    });
  });
