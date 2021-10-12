// fade-in effect on main page content


window.addEventListener("scroll", (event) => {
    const firstSelector = document.getElementById('fadeScroller1');
    const secondSelector = document.getElementById('fadeScroller2');
    const thirdSelector = document.getElementById('fadeScroller3')

    let scrollY = window.pageYOffset; // constant containing the y-position of page


    if (scrollY >= 400){
        firstSelector.classList.add('afterScroll');
    }
    if (scrollY >= 1000){
        secondSelector.classList.add('afterScroll');
    }
    if (scrollY >= 1500){
        thirdSelector.classList.add('afterScroll');
    }

    console.log(scrollY);
});
