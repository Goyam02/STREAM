document.addEventListener('DOMContentLoaded', function() {
    const logoutLink = document.getElementById('logout-link');

    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            const confirmation = confirm("Are you sure you want to log out?");
            if (!confirmation) {
                event.preventDefault(); 
            }
        });
    }
});
