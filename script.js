document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.login form');
    const passwordInput = document.getElementById('password');
    const correctPassword = 'STREAM123@';

    form.addEventListener('submit', (event) => {
        event.preventDefault(); 

        if (passwordInput.value === correctPassword) {
           
            window.location.href = 'index.html'; 
        } else {
            
            alert('Incorrect password. Please try again.');
        }
    });
});
