
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

function getitem() {
    var chk_arr = [];
    $("input[name=tag-list]:checked").each(function () {

        var chk = $(this).val();
        chk_arr.push(chk);
        console.log(chk)
    })

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