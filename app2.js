document.addEventListener('DOMContentLoaded', () => {
    const accountForm = document.querySelector('form[action="/update-account-settings"]');
    const privacyForm = document.querySelector('form[action="/update-privacy-settings"]');
    const deleteAccountButton = document.querySelector('.btn-delete');

    accountForm.addEventListener('submit', (event) => {
        event.preventDefault();
        if (validateAccountForm()) {
            submitForm(accountForm);
        }
    });

    privacyForm.addEventListener('submit', (event) => {
        event.preventDefault();
        submitForm(privacyForm);
    });

    deleteAccountButton.addEventListener('click', () => {
        if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
            deleteAccount();
        }
    });

    function validateAccountForm() {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password').value;

        if (password !== confirmPassword) {
            alert('Passwords do not match.');
            return false;
        }
        return true;
    }

    function submitForm(form) {
        const formData = new FormData(form);
        const action = form.getAttribute('action');

        fetch(action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Settings updated successfully.');
            } else {
                alert('An error occurred while updating settings.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating settings.');
        });
    }

    function deleteAccount() {
        fetch('/delete-account', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Account deleted successfully.');
                window.location.href = '/index.html';
            } else {
                alert('An error occurred while deleting the account.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the account.');
        });
    }
});
