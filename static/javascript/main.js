// created 3 constants that select the specific divs on main page to be faded

const imageGallery = document.getElementById('img-gal');
const outroMessage = document.getElementById('outro-msg');

// function that adds a specific class to the argument that is passed to it
function addClass(selector){
    selector.classList.add('afterScroll');
}


// event listener that finds the y-position and trigers events when it hits certain values
window.addEventListener("scroll", (event) => {

    let scrollY = window.pageYOffset; // constant containing the y-position of page
    console.log(scrollY);

    if (scrollY >= 700){ addClass(imageGallery); }
    if (scrollY >= 1750){ addClass(outroMessage); }

});
