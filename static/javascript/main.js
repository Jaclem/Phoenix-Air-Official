// created 3 constants that select the specific divs on main page to be faded

const firstSelector = document.getElementById('fadeScroller1');
const secondSelector = document.getElementById('fadeScroller2');
const thirdSelector = document.getElementById('fadeScroller3');

// function that adds a specific class to the argument that is passed to it
function addClass(selector){
    selector.classList.add('afterScroll');
}

// event listener that finds the y-position and trigers events when it hits certain values
window.addEventListener("scroll", (event) => {

    let scrollY = window.pageYOffset; // constant containing the y-position of page

    if (scrollY >= 480){ addClass(firstSelector); }
    if (scrollY >= 880){ addClass(secondSelector); }
    if (scrollY >= 1380){ addClass(thirdSelector); }
});
