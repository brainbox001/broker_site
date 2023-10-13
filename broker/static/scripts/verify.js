
  document.addEventListener('DOMContentLoaded', function () {
    const verifyForm = document.getElementById('verify-form');
    const verifyButton = document.getElementById('verify-button');
    const errorMessage = document.getElementById('error-message');

    verifyForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the form from submitting normally

      // Gather form data
      const formData = new FormData(verifyForm);

      // Use the Fetch API to send a POST request to your server
      fetch(verifyEmailEndpoint, {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json()) // Assuming your server returns JSON
        .then((data) => {
          if (data.success) {
            // Redirect to the dashboard on success
            window.location.href = '/dashboard';
          } else {
            // Display the error message
            errorMessage.textContent = data.message;
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    });
  });

