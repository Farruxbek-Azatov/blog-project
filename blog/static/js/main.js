
let leftOpenBtn = document.querySelector(".left-open-btn");
let listBox = document.querySelector(".list-box");
let arrow = document.querySelector(".fa-arrow-left");
let listClose = true;

window.addEventListener("resize", (e)=> {
	if (e.target.innerWidth > 1008) {
		location.reload();
	}
})
leftOpenBtn.addEventListener('click', ()=> {
	if (listClose) {
		listBox.style.width = "300px";
		listClose = false;
	} else {
		listBox.style.width = "0";
		listClose = true;
	}
	arrow.classList.toggle("fa-arrow-right");
})