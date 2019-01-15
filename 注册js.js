
    $(function () {
        var error_name = false;
        var error_password = false;
        var error_repassword = false;
        var error_phone =false;
        var error_email = false;
        var error_card = false;
        var error_address = false;
        
        $("#username").blur(function () {
            check_username()
        });
        $("#password").blur(function () {
            check_pwd()
        });
        $("#repassword").blur(function () {
            check_repwd()
        });
        $("#phone").blur(function () {
            check_phone()
        });
        $("#email").blur(function () {
            check_email()
        });
        $("#card_id").blur(function () {
            check_card()
        });
        $("#address").blur(function () {
            check_address()
        });

        //检查用户名
        function check_username() {
            var len = $('#username').val().length;


            if(len<2||len>20)
            {
                $('#username').next().html('输入2-20个字符的用户名').css("color","red");
                $('#username').next().show();
                error_name = true;

            }
            else
            {
                var username = $("#username").val();
                console.log(username)
                $.ajax({
                    url:"/user/check_user/",
                    type:"get",
                    data:{"username":username},
                    success:function (data) {
                        if(data.count){
                            console.log(data.count)
                            $('#username').next().html('用户名已存在,请重新输入').css("color","red").show();
                            error_name = true;
                        }else {
                            $('#username').next().hide();
                            error_name = false;
                        }

                    }
                })


            }
            };

        //检查密码
        function check_pwd() {
            var len = $('#password').val().length;
            if(len<4||len>20)
            {
                $('#password').next().html('密码最少4位，最长20位').css("color","red");
                $('#password').next().show();
                error_password = true;
            }
            else
            {
                $('#password').next().hide();
                error_password = false;
            }
        };
        //检查重复密码
        function check_repwd() {
            var pass = $('#password').val();
            var cpass = $('#repassword').val();

            if(pass!=cpass)
            {
                $('#repassword').next().html('两次输入的密码不一致').css("color","red");
                $('#repassword').next().show();
                error_repassword = true;
            }
            else
            {
                $('#repassword').next().hide();
                error_repassword = false;
            }

        };
        //检查手机号
        function check_phone() {
            var phone = $("#phone").val();
            if(!(/^1[3|4|5|6|7|8|9][0-9]\d{8}$/.test(phone))){

                //以1开头，3-9第二位，第三位0-9，剩下八位
                $("#phone").next().html("手机号码格式不正确").css("color","red");
                error_phone = true;

            }else {
                $("#phone").next().hide();
                error_phone = false;
            }

        };

        //检查邮箱
        function check_email() {
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确').css("color","red");
			$('#email').next().show();
			error_email = true;
		}

	    };
        //检查身份证
        function check_card() {
            var card = $("#card_id").val();
            var reg = /(^\d{15}$)|(^\d{17}(\d|X|x)$)/;
            if(reg.test(card) === false){
                $('#card_id').next().html('你输入的身份证格式不正确').css("color","red");
                $('#card_id').next().show();
                error_card = true;
            }else{
                $('#card_id').next().hide();
			    error_card = false;

            }
        };
        // {#//检验地址是否有值#
        function check_address() {
            var address = $("#address").val()
            if(address){
                $('#address').next().hide();
                error_address = false;
            }else {
                $('#address').next().html('请输入地址').css("color","red");
                $('#address').next().show();
                error_address = true;
            }

        };

        $("#button").click(function () {
            check_username();
            check_pwd();
            check_repwd();
            check_phone();
            check_card();
            check_address();
            var entry_time = $("#entry_time").val();
            var state = $("#state").val();
            var role = $("#role").val();
            var gender = $('input:radio:checked');
            console.log(state)
            if(entry_time === false){
                $('#entry_time').next().html('请选择日期').css("color","red");
                $('#entry_time').next().show();
            };
            if(state === false){
                $('#state').next().html('请选择状态').css("color","red");
                $('#state').next().show();
            };
            if(role === false){
                $('#role').next().html('请选择职务').css("color","red");
                $('#role').next().show();
            };
            if(gender === false){
                $('#gender').next().html('请选择性别').css("color","red");
                $('#gender').next().show();
            };


        })
        })




            