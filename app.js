
document.addEventListener('DOMContentLoaded', () => {
    const search = document.querySelector('.search');
    const search_input = document.getElementById('search_input');

    search.style.visibility = "hidden";
    search.style.opacity = 0;

    fetch('movie.json')
        .then(response => response.json())
        .then(data => {
            populateSearchResults(data);

            search_input.addEventListener('keyup', () => {
                let filter = search_input.value.toUpperCase();
                let a = search.getElementsByTagName('a');
                let hasVisibleItems = false;

                for (let index = 0; index < a.length; index++) {
                    let b = a[index].getElementsByClassName('cont')[0];
                    let textValue = b.textContent || b.innerText;

                    if (textValue.toUpperCase().indexOf(filter) > -1) {
                        a[index].style.display = "flex";
                        hasVisibleItems = true;
                    } else {
                        a[index].style.display = "none";
                    }
                }

                if (hasVisibleItems) {
                    search.style.visibility = "visible";
                    search.style.opacity = 1;
                } else {
                    search.style.visibility = "hidden";
                    search.style.opacity = 0;
                }

                if (search_input.value.trim() === "") {
                    search.style.visibility = "hidden";
                    search.style.opacity = 0;
                }
            });
        });

    function populateSearchResults(data) {
        search.innerHTML = '';

        data.forEach((element) => {
            let { name, imdb, date, sposter, genre, url } = element;
            let card = document.createElement("a");
            card.classList.add("card");
            card.href = url;
            card.innerHTML = `
                <img src="${sposter}">
                <div class="cont">
                    <h3>${name}</h3>
                    <p>${date}, ${genre} <span>IMDB</span><i class="bi bi-star-fill"></i>${imdb}</p>
                </div>
            `;
            search.appendChild(card);
        });
    }
});
document.addEventListener('DOMContentLoaded', () => {
    const popularSwiper = new Swiper('.popular-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.popular-next',
            prevEl: '.popular-prev',
        },
    });

    const trendingSwiper = new Swiper('.trending-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.trending-next',
            prevEl: '.trending-prev',
        },
    });
    const actionSwiper = new Swiper('.action-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.action-next',
            prevEl: '.action-prev',
        },
    });


    const horrorSwiper = new Swiper('.horror-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.horror-next',
            prevEl: '.horror-prev',
        },
    });

    const romanticSwiper = new Swiper('.romantic-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.romantic-next',
            prevEl: '.romantic-prev',
        },
    });

    const fantasySwiper = new Swiper('.fantasy-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.fantasy-next',
            prevEl: '.fantasy-prev',
        },
    });

    const ussitcomsSwiper = new Swiper('.ussitcoms-swiper', {
        slidesPerView: 7,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: '.ussitcoms-next',
            prevEl: '.ussitcoms-prev',
        },
    });

});

function selectPlan(planName, price) {
    const confirmation = confirm(`You have selected the ${planName} plan for $${price}/month. Proceed to payment?`);
    if (confirmation) {
        processPayment(planName, price);
    }
}

function processPayment(planName, price) {
    console.log(`Processing payment for ${planName} plan at $${price}/month...`);

    setTimeout(() => {
        alert(`Payment successful! You are now subscribed to the ${planName} plan.`);
    }, 2000);
}


function onScanSuccess(decodedText, decodedResult) {
    console.log(`Code matched = ${decodedText}`, decodedResult);
    document.getElementById('qr-reader-results').innerText = `Scanned Code: ${decodedText}`;
}

function onScanFailure(error) {
    console.warn(`Code scan error = ${error}`);
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "qr-reader", { fps: 10, qrbox: 250 });
html5QrcodeScanner.render(onScanSuccess, onScanFailure);


