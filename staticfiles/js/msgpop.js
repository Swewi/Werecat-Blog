 // Function to close alert when clicking on the alert itself
 document.querySelectorAll('.alert').forEach(alert => {
    // Initialize the alert instance
    const alertInstance = new bootstrap.Alert(alert);

    // Add click event listener to alert
    alert.addEventListener('click', function() {
        alertInstance.close();
    });
});