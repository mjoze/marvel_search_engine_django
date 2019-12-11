const btn = document.querySelectorAll('.comics_button');
const comics_list = document.querySelectorAll('.comics');
for (let i = 0; i < btn.length; i++) {
    btn[i].addEventListener('click', () => {
        comics_list[i].classList.toggle('active');
        if (btn[i].innerHTML == "SHOW LIST") {
            btn[i].innerHTML = "HIDE";
        } else {
            btn[i].innerHTML = "SHOW LIST";

        }
    })
}
const lista = document.querySelectorAll('li')
for (let i = 0; i < lista.length; i++) {
    lista[i].addEventListener("click", () => {
        lista[i].classList.toggle('line_through')
    });
}


const divN = document.querySelector('.notification');
console.log(divN)
setTimeout(() => {
    divN.style.display = "none"
}, 3000)