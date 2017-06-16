$(function(){
    $('html').keyup(function(e){
        switch(e.which){
            case 37: // Key[←]
                $("#prev").click();
                break;
 
            case 39: // Key[→]
                $("#next").click();
                break;
        }
    });

    $('#help').on({
        'show.bs.collapse': function () {
            $("#helpbtn").text("基準を閉じる");
        },
        'hide.bs.collapse': function () {
            $("#helpbtn").text("基準を開く");
        }
    });
});