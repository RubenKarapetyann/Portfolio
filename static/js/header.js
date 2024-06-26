const navMenuButton = document.getElementById("nav-menu-button")

navMenuButton.addEventListener("click", function(event){
    console.log("hello");
})

const header = document.querySelector("header");
const toggleClass = "is-sticky";
window.addEventListener("scroll", () => {
  const currentScroll = window.scrollY;
  if (currentScroll > 100) {
    header.classList.add(toggleClass);
  } else {
    header.classList.remove(toggleClass);
  }
})