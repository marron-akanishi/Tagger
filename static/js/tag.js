function setTag(index, id){
    $.ajax({
        url: '/settag',
        type: 'POST',
        data: {
            "id":id,
            "image":$("#image").attr("src"),
            "tagid":index
        },
        success:function(resultdata) {
            if(resultdata == "end"){
                alert("終了");
            }else{
                location.href=resultdata;
            }
        },
        error: function(error) {
            alert('送信失敗');
        }
    });
}
