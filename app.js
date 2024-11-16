let left_btn = document.getElementsByClassName('bi-chevron-left')[0];
let right_btn = document.getElementsByClassName('bi-chevron-right')[0];
let cards = document.getElementsByClassName('cards')[0];
let search = document.getElementsByClassName('search')[0];
let search_input = document.getElementById('search_input');
//error
left_btn.addEventListener('click', () => {
    cards.scrollLeft -= 140;
});

right_btn.addEventListener('click', () => {
    cards.scrollLeft += 140;
});

let json_url = "movie.json";

fetch(json_url)
    .then(response => response.json())
    .then((data) => {
        data.forEach((ele) => {
            let { name, imdb, date, sposter, bposter, genre, url } = ele;
            let card = document.createElement("a");
            card.classList.add("card");
            card.href = url;
            card.innerHTML = `
                <img src="${sposter}" alt="${name}" class="posters">
                <div class="rest_card">
                    <img src="${bposter}">
                    <div class="cont">
                        <h4>${name}</h4>
                        <div class="sub">
                            <p>${date} ‧ ${genre} ‧ 2 seasons</p>
                            <h3><span>IMDB</span><i class="bi bi-star-fill"></i>${imdb}</h3>
                        </div>
                    </div>
                </div>
            `
        });

        document.getElementById("title").innerText = data[0].name;
        document.getElementById("gen").innerText = data[0].genre;
        document.getElementById("date").innerText = data[0].date;
        document.getElementById("rate").innerHTML = `<span>IMDB</span><i class="bi bi-star-fill"></i>${data[0].imdb}`;

        populateSearchResults(data);
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
        `
        search.appendChild(card);
    });

    search_input.addEventListener('keyup', () => {
        let filter = search_input.value.toUpperCase();
        let a = search.getElementsByTagName('a');
        for (let index = 0; index < a.length; index++) {
            let b = a[index].getElementsByClassName('cont')[0];
            let textValue = b.textContent || b.innerText;

            if (textValue.toUpperCase().indexOf(filter) > -1) {
                a[index].style.display = "flex";
                search.style.visibility = "visible";
                search.style.opacity = 1;
            } else {
                a[index].style.display = "none";
            }
        }

        // error
        if (search_input.value === "") {
            search.style.visibility = "hidden";
            search.style.opacity = 0;
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const taDumSound = document.getElementById('ta-dum-sound');
    
    taDumSound.currentTime = 0;
    
    taDumSound.play().catch(error => {
        console.error('Failed to play sound:', error);
    });
});





// document.addEventListener('DOMContentLoaded', () => {
//     const animatedElements = document.querySelectorAll('.fade-in');

//     const handleScroll = () => {
//         animatedElements.forEach(element => {
//             const rect = element.getBoundingClientRect();
//             if (rect.top < window.innerHeight) {
//                 element.classList.add('visible');
//             }
//         });
//     };

//     window.addEventListener('scroll', handleScroll);

//     // Initial check in case elements are already in view
//     handleScroll();
// });

// let left_btn = document.getElementsByClassName('bi-chevron-left')[0];
// let right_btn = document.getElementsByClassName('bi-chevron-right')[0];
// let cards = document.getElementsByClassName('cards')[0];
// let search = document.getElementsByClassName('search')[0];
// let search_input = document.getElementById('search_input');

// left_btn.addEventListener('click', () => {
//     cards.scrollLeft -= 140;
// });

// right_btn.addEventListener('click', () => {
//     cards.scrollLeft += 140;
// });

// let json_url = "movie.json";

// fetch(json_url)
//     .then(response => response.json())
//     .then((data) => {
//         // Display initial movie cards
//         data.forEach((ele) => {
//             let { name, imdb, date, sposter, bposter, genre, url } = ele;
//             let card = document.createElement("a");
//             card.classList.add("card", "fade-in"); // Add fade-in class here
//             card.href = url;
//             card.innerHTML = `
//                 <img src="${sposter}" alt="${name}" class="posters">
//                 <div class="rest_card">
//                     <img src="${bposter}">
//                     <div class="cont">
//                         <h4>${name}</h4>
//                         <div class="sub">
//                             <p>${date} ‧ ${genre} ‧ 2 seasons</p>
//                             <h3><span>IMDB</span><i class="bi bi-star-fill"></i>${imdb}</h3>
//                         </div>
//                     </div>
//                 </div>
//             `;
//             cards.appendChild(card);
//         });

//         // Display the first movie details
//         document.getElementById("title").innerText = data[0].name;
//         document.getElementById("gen").innerText = data[0].genre;
//         document.getElementById("date").innerText = data[0].date;
//         document.getElementById("rate").innerHTML = `<span>IMDB</span><i class="bi bi-star-fill"></i>${data[0].imdb}`;

//         // Populate search results
//         populateSearchResults(data);
//     });

// function populateSearchResults(data) {
//     // Clear previous search results
//     search.innerHTML = '';

//     data.forEach((element) => {
//         let { name, imdb, date, sposter, genre, url } = element;
//         let card = document.createElement("a");
//         card.classList.add("card", "fade-in"); // Add fade-in class here
//         card.href = url;
//         card.innerHTML = `
//             <img src="${sposter}">
//             <div class="cont">
//                 <h3>${name}</h3>
//                 <p>${date}, ${genre} <span>IMDB</span><i class="bi bi-star-fill"></i>${imdb}</p>
//             </div>
//         `;
//         search.appendChild(card);
//     });

//     // Add search functionality
//     search_input.addEventListener('keyup', () => {
//         let filter = search_input.value.toUpperCase();
//         let a = search.getElementsByTagName('a');

//         // Clear previous search results
//         for (let index = 0; index < a.length; index++) {
//             let b = a[index].getElementsByClassName('cont')[0];
//             let textValue = b.textContent || b.innerText;

//             if (textValue.toUpperCase().indexOf(filter) > -1) {
//                 a[index].style.display = "flex";
//                 search.style.visibility = "visible";
//                 search.style.opacity = 1;
//             } else {
//                 a[index].style.display = "none";
//             }
//         }

//         // Hide search results if input is empty
//         if (search_input.value === "") {
//             search.style.visibility = "hidden";
//             search.style.opacity = 0;
//         }
//     });
// }
