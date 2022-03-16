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