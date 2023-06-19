const btns = document.querySelectorAll('.btn');
const storeProducts = document.querySelectorAll('.store-job');
// const search = document.getElementById(search);

for (i = 0; i < btns.length; i++) {

    btns[i].addEventListener('click', (e) => {
        e.preventDefault()
        
        const filter = e.target.dataset.filter;
        console.log(filter);
        
        storeProducts.forEach((job)=> {
            if (filter === 'all'){
                job.style.display = 'block'
            } else {
                if (job.classList.contains(filter)){
                    job.style.display = 'block'
                } else {
                    job.style.display = 'none'
                }
            }
        });
    });
};

// SEARCH FILTER
const search = document.getElementById("search");
const productName = document.querySelectorAll(".job-details h2");

// A BETTER WAY TO FILTER THROUGH THE PRODUCTS
search.addEventListener("keyup", filterProducts);


function filterProducts(e) {
    const text = e.target.value.toLowerCase();
    // console.log(productName[0]);
    productName.forEach(function(job) {
        const item = job.firstChild.textContent;
        if (item.toLowerCase().indexOf(text) != -1) {
            job.parentElement.parentElement.style.display = "block"
        } else {
            job.parentElement.parentElement.style.display = "none"
        }
    })
}



// This code has been replaced by the function(filterProducts) above which does a better job

// search.addEventListener("keyup", (e) => {
//     e.preventDefault();
//     const searchValue = search.value.toLowerCase().trim();
//     // alert(search.value);

    
//     for (i = 0; i < storeProducts.length; i++) {
//         if (storeProducts[i].classList.contains(searchValue)) {
//             storeProducts[i].style.display = 'block';
//         } else if (searchValue == "") {
//             storeProducts[i].style.display = 'block';
//         } else {
//             storeProducts[i].style.display = 'none';    
//         }

//     //    if (searchValue == "") {
//     //     storeProducts[i].style.display = 'block';
//     //    }
        
//     }

// })

