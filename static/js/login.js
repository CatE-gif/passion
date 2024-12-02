$(document).ready(function() {
    $('form').on('submit', function(e) {
        e.preventDefault(); // 防止默认提交
        var form = $(this);
        var formData = form.serialize();

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: formData,
            success: function(response) {
                // 登录成功后跳转
                window.location.href = '/';
            },
            error: function(xhr) {
                if (xhr.status === 400) {
                    var errorMessage = xhr.responseJSON.error;
                    // 弹窗提示错误信息
                    alert(errorMessage);
                } else {
                    alert("服务器错误，请稍后再试。");
                }
            }
        });
    });
});
