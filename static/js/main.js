const container = document.querySelector(".background");
const box = container.querySelector(".area_box");

const {width:containerWidth, height:containerHeight} =
container.getBoundingClientRect();
const {width:boxWidth, height:boxHeight} =
box.getBoundingClientRect();
let isDragging = null;
let originLeft = null;
let originTop = null;
let originX = null;
let originY = null;

box.addEventListener("mousedown", (e) =>{
    isDragging =true;
    originX = e.clientX;
    originY = e.clientY;
    originLeft = box.offsetLeft;
    originTop = box.offsetTop;
});

document.addEventListener("mouseup", (e)=>{
    isDragging = false;

});

document.addEventListener("mousemove", (e) => {
    if(isDragging){
        const diffX = e.clientX - originX;
        const diffY = e.clientY - originY;
        const end0fXPoint = containerWidth - boxWidth;
        const end0fYPoint = containerHeight - boxHeight;
        box.style.left = `${Math.min(Math.max(0, originLeft+diffX), end0fXPoint)}px`;
        box.style.top = `${Math.min(Math.max(0, originTop+diffY), end0fYPoint)}px`;
    }
});


function clip(){

    let url = '';
    const textarea = document.createElement("textarea");
    document.body.appendChild(textarea);
	url = window.document.location.href;
	textarea.value = url;
	textarea.select();
	document.execCommand("copy");
	document.body.removeChild(textarea);
	alert("URL이 복사되었습니다.")
}

