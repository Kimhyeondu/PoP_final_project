$(document).ready(function () {
    $('#modal').hide();
})

// '삭제' 클릭하면 모달 나오게
jQuery('#delete-btn').click(function() {
   if($('#modal').css('display') === 'none') {
       jQuery('#modal').show();
   } else {
       jQuery('#modal').hide();
   }
});

// 모달에서 '아니오' 클릭하면 모달 끄기
jQuery('#close-modal').click(function() {
    $('#modal').hide();
});

// 카드 삭제하기
function delete(){
    // var url = jQuery('#origin').attr("src");
    // var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    //
    // $.ajax({
    //     url: 'http://127.0.0.1:8000/card/delete/id',
    //     data: {'url': src},
    //     beforeSend: function(xhr) {
    //         xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //     },
    //     method: "POST",
    //     success: function (response){
    //         alert('삭제완료!!!')
    //     }
    // })
}