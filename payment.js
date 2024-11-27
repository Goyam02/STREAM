document.addEventListener('DOMContentLoaded', function() {
    const planButtons = document.querySelectorAll('.btn-select');
    const payButton = document.getElementById('pay-btn');
    let selectedPlan = null;

    planButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Deselect any previously selected plan
            planButtons.forEach(btn => btn.parentElement.classList.remove('selected'));
            
            // Select the current plan
            this.parentElement.classList.add('selected');
            selectedPlan = this.parentElement;
        });
    });

    if (payButton) {
        payButton.onclick = function(e) {
            if (!selectedPlan) {
                alert('Please select a subscription plan.');
                return;
            }

            const planName = selectedPlan.querySelector('h3').innerText;
            const planAmount = selectedPlan.querySelector('p').innerText.replace('/month', '').replace('$', '');

            const options = {
                key: '[REDACTED:Generic API Key]', // Replace with your Razorpay API key
                amount: parseFloat(planAmount) * 100, // Amount in paise
                currency: "USD", // Change currency if needed
                name: "Stream Subscription",
                description: `Subscription Plan: ${planName}`,
                handler: function(response) {
                    const paymentId = response.razorpay_payment_id;
                    alert(`Payment successful! Payment ID: ${paymentId}`);
                    // You can redirect or perform other actions here
                },
                prefill: {
                    name: "John Doe", // Replace with actual user data
                    email: "john.doe@example.com", // Replace with actual user data
                },
                theme: {
                    color: "#007bff"
                }
            };

            const rzp = new Razorpay(options);
            rzp.open();
            e.preventDefault();
        };
    }
});
