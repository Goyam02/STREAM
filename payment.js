document.addEventListener('DOMContentLoaded', function() {
    const planButtons = document.querySelectorAll('.btn-select');
    const payButton = document.getElementById('pay-btn');
    let selectedPlan = null;

    planButtons.forEach(button => {
        button.addEventListener('click', function() {
            planButtons.forEach(btn => btn.parentElement.classList.remove('selected'));
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
                key: 'YOUR_RAZORPAY_API_KEY', // Replace with your Razorpay API key
                amount: parseFloat(planAmount) * 100,
                currency: "USD",
                name: "Stream Subscription",
                description: `Subscription Plan: ${planName}`,
                handler: function(response) {
                    const paymentId = response.razorpay_payment_id;
                    alert(`Payment successful! Payment ID: ${paymentId}`);
                },
                prefill: {
                    name: "John Doe",
                    email: "john.doe@example.com",
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
