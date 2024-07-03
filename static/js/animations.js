let options = {
    root : null,
    rootMargin : "0px",
    threshold : 0.1
}

const callback = (entries, observer)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            if(new Array(...entry.target.classList).includes("card-anim")){
                entry.target.classList.add("active-card")
            }else{
                entry.target.classList.add("active-title")
            }
        }
    })
}

const observer = new IntersectionObserver(callback, options)

const titles = new Array(...document.getElementsByClassName("title-anim"))
titles.forEach(title => {
    observer.observe(title)
})

const cards = new Array(...document.getElementsByClassName("card-anim"))
cards.forEach(card => {
    observer.observe(card)
})