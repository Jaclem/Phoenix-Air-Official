// fade-in effect on main page content


window.addEventListener("scroll", (event) => {
    const fadeSelector = document.querySelector('.beforeScroll');
    const scrollY = window.pageYOffset; //

    if (scrollY >= 400){
        fadeSelector.classList.add('afterScroll');
    }
    console.log(scrollY);
});
