var wel=document.getElementById("welcome");
setTimeout(()=>{
wel.style.display="block";
},1000);
function scroll(){
var navbar=document.getElementById("nav");
var brand=document.querySelector(".brand-container");
var ypos=window.pageYOffset;
if(ypos > 400){
    navbar.style.height="90px";
    navbar.style.opacity="1";
    navbar.style.lineHeight="90px";
}
else{
    navbar.style.height="60px";
    navbar.style.lineHeight="60px";
}

}
window.addEventListener("scroll",scroll);

setTimeout(()=>{
var container=document.querySelector(".container");
},2000);

