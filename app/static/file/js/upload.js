$(function () {
    var file = $('#file');
    var imgage_url = $("input[name='image_url']");
    file.on('change', function (e) {
        $("#add-bbb").css('display','none');
        $("#loder").css('display','block');
        var img_url = e.currentTarget.files[0].name;
        var file = document.getElementById("file").files[0];
        var fm = new FormData();
        fm.append('file', file);
        zlajax.post({
            'url': 'app/static/file/img/',
            processData: false,
            contentType: false,
            'data': fm,
            'success': function (data) {
                if (data['code'] == 200) {
                    swal('上传成功！');
                    imgage_url.val(data['data']);
                        $("#add-bbb").css('display','block');
                        $("#loder").css('display','none');
                    $("#img_show").attr("src", data['data']);
                }
            }
        })
    });
})