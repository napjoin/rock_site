let menu_btn = document.querySelector(".menu_btn")
let menu = document.querySelector(".menu")

console.log("1");

function move_menu() {
    if (menu.style.left == "0%"){
        menu.style.left = "-20%";
    }
    else {
        menu.style.left = "0%";
    }
    

}

menu_btn.addEventListener('click', move_menu)