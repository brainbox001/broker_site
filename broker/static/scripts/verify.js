
  document.addEventListener('DOMContentLoaded', function () {
    const verifyForm = document.getElementById('verify-form');
    const verifyButton = document.getElementById('verify-button');
    const errorMessage = document.getElementById('error-message');


    verifyForm.addEventListener('submit', function (e) {
        e.preventDefault();
        
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
        };

        xhr.send(formData);
    });
  });
