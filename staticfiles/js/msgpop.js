// Function to close alert when clicking on the alert itself
document.querySelectorAll(".alert").forEach(alert => {
    try {
        // Initialize the alert instance using Bootstrap's Alert class
        const alertInstance = new bootstrap.Alert(alert);

        // Add click event listener to the alert element
        alert.addEventListener("click", function() {
            // Close the alert when it's clicked
            alertInstance.close();
        });
    } catch (error) {
        console.error("Error initializing alert instance or adding event listener:", error);
    }
});