$(document).ready(function () {
    const {createEditor, createToolbar} = window.wangEditor;

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml();
            let title = $("input[name='title']").val();
            console.log('Editor content on change:', title);
            console.log('Editor content on change:', html); // 打印编辑器内容变化
        }
    };

    // 初始化WangEditor
    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>', // 默认HTML内容
        config: editorConfig,
        mode: 'default', // 'simple' 为简化模式
    });

    // 初始化工具栏
    const toolbarConfig = {};
    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // 'simple' 为简化模式
    });


    $("#submit-btn").click(function (event) {
        event.preventDefault();
        console.log("按钮点击事件被触发"); // 测试按钮是否响应

        let title = $("input[name='title']").val();
        let category = $("select[name='category']").val();  // category 必须是一个有效的 id
        const content = editor.getHtml();
        let csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();

        if (!title || !content || !category) {
            alert("标题、内容和分类不能为空！");
            return;
        }

        $.ajax({
            url: '/blog/pub',
            method: 'POST',
            data: {
                title: title,
                category: category,  // 确保传递的是有效的 category id
                content: content,
                csrfmiddlewaretoken: csrfmiddlewaretoken
            },
            success: function (response) {
                if (response.code === 200) {
                    alert(response.message);
                    let blog_id = response['data']['blog_id'];
                    window.location.href = '/blog/'+blog_id;
                } else {
                    alert("表单验证失败：" + JSON.stringify(response.message));
                }
            },
            error: function (xhr, status, error) {
                alert("网络错误，请稍后再试！");
                console.error("Error:", error);
            }
        });
    });

});



