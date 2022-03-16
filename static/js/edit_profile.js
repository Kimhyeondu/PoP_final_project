



function eventHandler(e) {
    var $eTarget = $(e.currentTarget);
    // var $targetPanel = $('[aria-labelledby="' + $eTarget.attr('id') + '"]');
    if($eTarget.hasClass("active")===true){
        $eTarget
            .attr('aria-selected', false)
            .removeClass('active')
    }
    else if($eTarget.hasClass("active")===false){
        $eTarget
            .attr('aria-selected', true)
            .addClass('active') // 구버전 IE
    }

        /*
        .siblings('[role="option"]')   //형제요소들
        .attr('aria-selected', false)  //영역선택 해제
        .removeClass('active'); // 구버전 IE*/

    // $targetPanel
    //     .attr('aria-hidden', false)
    //     .addClass('panel') // 구버전 IE
    //     .siblings('[role="tabpanel"]')
    //     .attr('aria-hidden', true)
    //     .removeClass('panel'); // 구버전 IE
}

function shuffle(array) { //배열의 원소를 무작위로 섞어주는 함수 (추천태그가 유저가 선택한것중에 무작위로 나올 수있도록 설정)
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;    //섞어진 배열을 리턴한다
}

function getitem() {
    var rr = [];
    var l=0;
    for(var i=1; i<11; i++){
        var t='#tag'+i    //태그10번까지 탐색
        var tag=  $(t)
        if(tag.hasClass("active")===true){  //클릭된 요소는 active라는 클래스가 추가되므로 이를이용하여 판별
            let tagg=tag.text().split("\n",1);   //널문자 제거를위해 \n을기준으로 자름
            console.log(tagg)
            rr[l] = tagg;
            alert(rr[l]);
            l+=1;       //클릭된 요소가 있을때만 추가되도록 설정
        }

    }
    for (let i = 0; i < rr.length; i++) {
        console.log(rr[i])
    }

    shuffle(rr)
    for (let i = 0; i < rr.length; i++) {
        console.log(rr[i])
    }
    $.ajax({
        type: "POST",
        url: "/edit_user",
        dataType: 'json',
        data: rr,
        cache: false,
        contentType: false,
        processData: false,
        success: function (rr) {
            alert(rr)
        },
        error:function (){
            alert("error_send")
        }
    });





    console.log(rr);
}

$('[role="option"]').on('click', eventHandler);
//
$('[role="button"]').on('click', getitem);
function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    $('#blah').attr('src', e.target.result);
                }
                reader.readAsDataURL(input.files[0]);
            }
        }