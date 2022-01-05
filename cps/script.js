let allow = true
document.body.innerHTML = "0"
addEventListener("click",(_)=>{
    if (document.body.innerHTML == 1) {
        setTimeout(() => {
            allow = false
        }, 1000);
    }
    if (allow) {  
    document.body.innerHTML = `${Number(document.body.innerHTML) +1}`
}})