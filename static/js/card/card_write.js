// 페이지간 이동
const deco_page = document.querySelector("#deco_page");
const deco_prev = document.querySelector("#deco_prev");
const deco_next = document.querySelector("#deco_next");

const msg_page = document.querySelector("#msg_page");
const msg_prev = document.querySelector("#msg_prev");
const msg_next = document.querySelector("#msg_next");

const gift_page = document.querySelector("#gift_page");
const gift_prev = document.querySelector("#gift_prev");
const gift_next = document.querySelector("#gift_next");

const view_page = document.querySelector("#view_page");
const view_prev = document.querySelector("#view_prev");
const view_next = document.querySelector("#view_next");

deco_next.addEventListener("click", ()=>{deco_page.className = "sub_container moved";});
gift_next.addEventListener("click", ()=>{gift_page.className = "sub_container moved";});

msg_prev.addEventListener("click", ()=>{deco_page.className = "sub_container back";});        
gift_prev.addEventListener("click", ()=>{msg_page.className = "sub_container back";});        
view_prev.addEventListener("click", ()=>{gift_page.className = "sub_container back";});
// 장식페이지
// function readImage(input) {
//     // 인풋 태그에 파일이 있는 경우
//     if(input.files && input.files[0]) {
//         // FileReader 인스턴스 생성
//         const reader = new FileReader();
//         // 이미지가 로드가 된 경우
//         reader.onload = (event) => {
//             const previewImage = document.getElementById("preview_image")
//             previewImage.src = event.target.result
//         };
//         // reader가 이미지 읽도록 하기
//         reader.readAsDataURL(input.files[0]);
//     }
// };

// const customImage = document.getElementById("custom_image")
// customImage.addEventListener("change", (event) => {
//     readImage(event.target)
// });

const previewImage = document.getElementById("preview_image")
const decoList = Array.from(document.querySelector(".deco_selec_wrap").children);

decoList.forEach(element => {
    element.addEventListener("click", (e) => {
        decoList.forEach(el => {
            el.className = "deco_selec"
        })
        previewImage.alt = e.target.innerText
        e.target.className = "deco_selec selected"
    
    })
});



// 메시지 페이지
const msgNext = document.getElementById("msg_next")
const message = document.getElementById("message")
const csrftoken = document.querySelector("#cs input").value
const modal_wrap = document.createElement("div")
modal_wrap.className = "modal_wrap"
modal_wrap.innerHTML = "<div class='modal_div'>잠시만 기다려 주세요</div>"

function postToGift() {
    let data = new FormData();
    data.append("img",preview_image.src);
    data.append("msg",message.innerText);
    data.append('csrfmiddlewaretoken', csrftoken);
    document.querySelector("body").appendChild(modal_wrap)

    fetch("/card/write/", {
        method:"POST",
        body: data,
        credentials: 'same-origin',
        redirect: "follow",
    }).then(response=>{
        // HTTP 301 response
        document.querySelector("body").removeChild(document.querySelector(".modal_wrap"))
        msg_page.className = "sub_container moved";
    }).catch(e => {
        console.info(err + " url: " + url);
    })
}

msgNext.addEventListener("click", postToGift)

