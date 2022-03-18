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
const pathname = window.location.pathname
const toUserId = pathname.split("/")[pathname.split("/").length - 1]
const msgNext = document.getElementById("msg_next")
const message = document.getElementById("message")
const messageResult = document.getElementById("message_result")
const modal_wrap = document.createElement("div")
modal_wrap.className = "modal_wrap"
modal_wrap.innerHTML = "<div class='modal_div'>잠시만 기다려 주세요</div>"


function fetchRecommend(data) {
    return new Promise((receive) => { 
        fetch("/api/v1/card/", {
            method:"POST",
            body: data,
            credentials: 'same-origin',
            redirect: "follow",
        }).then((response) => {
            receive(response.json());
        }).catch((err)=>{
            console.info(err);
        }); 
    }); 
}

async function postToGift() {
    let data = new FormData();
    data.append("id", toUserId);
    data.append("msg", message.value);
    // data.append('csrfmiddlewaretoken', csrftoken);
    document.querySelector("body").appendChild(modal_wrap);

    let jsonData = await fetchRecommend(data);

    showRecommendList(jsonData);
    console.log(jsonData);
    document.querySelector("body").removeChild(document.querySelector(".modal_wrap"));
    msg_page.className = "sub_container moved";
}

async function msgToGift() {
    if (message.value.length > 0) {
        messageResult.value = message.value
        await postToGift();
    } else {
        alert("메시지를 입력하세요");
    };
}

msgNext.addEventListener("click", msgToGift);

// 선물 페이지
const $search = document.querySelector("#search_gift")
const $searchButton = document.querySelector(".search_button")
const gcCont = document.querySelector(".gift_cont_container")

function showRecommendList(jsondata) {
    gcCont.innerHTML = ""
    // let reList = jsondata[0]
    // let tagList = jsondata[1]
    jsondata.forEach(giftList => {
        let $reListCon = document.createElement("div")
        $reListCon.className = "gift_box_container"
        $reListCon.innerHTML = '<div class="gift_tag">추천 선물</div>'
        let $reWrap = document.createElement("div")
        $reWrap.className = "gift_box_wrap"
        $reListCon.appendChild($reWrap)
        giftList.forEach(e => {
            let gBox = document.createElement("div")
            gBox.className = "gift_box"
            gBox.innerHTML = `<img src="${e.gift_img}" alt="${e.gift_name}" class="gift_img">${e.gift_name}`
            $reWrap.append(gBox)
        });
        gcCont.appendChild($reListCon)
    });
}

function fetchSearch(data) {
    return new Promise((receive) => { 
        fetch("/api/v1/card/search/", {
            method:"POST",
            body: data,
            credentials: 'same-origin',
            redirect: "follow",
        }).then((response) => {
            receive(response);
        }).catch((err)=>{
            console.info(err);
        }); 
    }); 
}

function showSearchList(jsondata) {
    console.log(jsondata)
    gcCont.innerHTML = ""
    let $reListCon = document.createElement("div")
    $reListCon.className = "gift_box_container"
    $reListCon.innerHTML = '<div class="gift_tag">검색 결과</div>'
    let $reWrap = document.createElement("div")
    $reWrap.className = "gift_box_wrap"
    $reListCon.appendChild($reWrap)
    jsondata.forEach(e => {
        let gBox = document.createElement("div")
        gBox.className = "gift_box"
        gBox.innerHTML = `<img src="${e.gift_img}" alt="${e.gift_name}" class="gift_img">${e.gift_name}`
        $reWrap.append(gBox)
    });
    gcCont.appendChild($reListCon);
}


function showSearchErr(jsondata) {
    console.log(jsondata)
    gcCont.innerHTML = ""
    let $reListCon = document.createElement("div")
    $reListCon.className = "gift_box_container"
    $reListCon.innerHTML = `<div class="gift_tag">${jsondata.err_msg}</div>`
    gcCont.appendChild($reListCon);
}


async function searchGift() {
    let keyword = $search.value
    let data = new FormData();
    data.append("keyword", keyword);

    let response = await fetchSearch(data);
    let code = await response.status
    let jsondata = await response.json()
    if (code === 200) {
        showSearchList(jsondata);
    } else {
        showSearchErr(jsondata);
    }
}

$search.addEventListener('keyup', (e)=>{
    if (e.keyCode === 13) {
        searchGift();
    }  
});

$searchButton.addEventListener("click", searchGift)

// 미리보기 페이지
const csrftoken = document.querySelector("#cs input").value;

function fetchPostMessage(data) {
    return new Promise((receive) => { 
        fetch(pathname, {
            method:"POST",
            body: data,
            credentials: 'same-origin',
            redirect: "follow",
        }).then((response) => {
            receive(response.json());
        }).catch((e)=>{
            console.info(err + " url : " + url);
        }); 
    }); 
}


function postMessage() {
    let giftId = 1
    let decoSelected = document.getElementsByClassName("deco_selec selected")
    let title = document.querySelector("#title")
    let author = document.querySelector("#author")

    let data = new FormData();
    data.append("csrfmiddlewaretoekn", csrftoken)
    data.append("to_user_id", toUserId)
    data.append("gift_id", giftId)
    data.append("msg", message.value)
    data.append("deco", decoSelected.innerText)
    // data.append("title", title.innerText)
    // data.append("author", author.innerText)

    console.log(data)
    console.log(csrftoken)
    console.log(toUserId)
    console.log(giftId)
    console.log(message.value)
    console.log(decoSelected.innerText)


}


view_next.addEventListener("click", postMessage)
