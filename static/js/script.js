// This file is developed by Divyasri Lakshmi Alekhya Nakka (018291702)
document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('textarea[name="content"]');
    const charCounter = document.querySelector('.char-counter');
    const submitButton = document.querySelector('button[name="create"]');
    const maxLength = 500;

    function updateCharCounter() {
        const remaining = maxLength - textarea.value.length;
        charCounter.textContent = `${remaining} characters remaining`;

        if (remaining < 50) {
            charCounter.classList.add('limit');
        } else {
            charCounter.classList.remove('limit');
        }

        submitButton.disabled = remaining < 0;
    }

    textarea.addEventListener('input', updateCharCounter);
    updateCharCounter();

    // Add loading state to buttons
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const button = e.submitter;
            button.classList.add('loading');
            button.disabled = true;
        });
    });
});
