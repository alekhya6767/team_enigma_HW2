// This file is developed by Divyasri Lakshmi Alekhya Nakka (018291702)

// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Select the textarea for post content, the character counter element, and the submit button
    const textarea = document.querySelector('textarea[name="content"]');
    const charCounter = document.querySelector('.char-counter');
    const submitButton = document.querySelector('button[name="create"]');
    const maxLength = 500; // Define the maximum allowed characters for a post

    // Function to update the character counter and handle input validation
    function updateCharCounter() {
        const remaining = maxLength - textarea.value.length; // Calculate remaining characters
        charCounter.textContent = `${remaining} characters remaining`; // Update the counter display

        // Add a visual warning if the remaining characters are below 50
        if (remaining < 50) {
            charCounter.classList.add('limit'); // Add a CSS class for styling the warning
        } else {
            charCounter.classList.remove('limit'); // Remove the warning class if not needed
        }

        // Disable the submit button if the character limit is exceeded
        submitButton.disabled = remaining < 0;
    }

    // Attach an event listener to the textarea to update the counter on input
    textarea.addEventListener('input', updateCharCounter);
    updateCharCounter(); // Initialize the counter when the page loads

    // Add a loading state to buttons when a form is submitted
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const button = e.submitter; // Get the button that triggered the form submission
            button.classList.add('loading'); // Add a CSS class to indicate loading state
            button.disabled = true; // Disable the button to prevent multiple submissions
        });
    });
});