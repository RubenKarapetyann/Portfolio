const navMenuButton = document.getElementById("nav-menu-button")
const mobileNav = document.getElementById("mobile-nav")
const mobileNavElements = document.getElementsByClassName("mobile-element-inner-container")

function navClosing(){
  mobileNav.classList.remove("isOpening")
  mobileNav.classList.add("isClosing")
  navMenuButton.classList.remove("isTurning90")
  navMenuButton.classList.add("isTurning-90")
  setTimeout(()=>{
    mobileNav.style.display = "none"
  }, 300)
  navMenuButton.style.transform = "rotate(0deg)"
}
function navOpening(){
  mobileNav.style.display = "block"
  navMenuButton.style.transform = "rotate(90deg)"
  navMenuButton.classList.remove("isTurning-90")
  navMenuButton.classList.add("isTurning90")
  mobileNav.classList.remove("isClosing")
  mobileNav.classList.add("isOpening")
}

for(let i = 0; i < mobileNavElements.length; i++){
  const el = mobileNavElements.item(i)
  el.addEventListener("click", navClosing)
}

navMenuButton.addEventListener("click", function(event){
  if(mobileNav.style.display === "block"){
    navClosing()
  }else {
    navOpening()
  }
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