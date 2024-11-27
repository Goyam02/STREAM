document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (username && email && password) {
            
            sendEmail(email, username, password);

            alert("Profile updated successfully!");

            form.reset();
        } else {
            alert("Please fill in all fields.");
        }
    });

    function sendEmail(email, username, password) {
        console.log(`Sending email to ${email} with new credentials:
        Username: ${username}
        Password: ${password}`);
        
        alert(`An email with your new credentials has been sent to ${email}.`);
    }
});
