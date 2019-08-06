<!DOCTYPE html>
<html>
<head>
	<title>reset password form</title>

<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
<link rel="stylesheet" type="text/css" href="../css/stylelogin.css">
	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>


	<div class="forgot_password" id="forgot_password">
		<div class="form-box_forgot">
			<form name="reset_password" action="../php/authentication.php" method="POST">
			<h1>Recover Your Password</h1>
			<div class="input-box-pass">
				<i class="fa fa-envelope-o"></i>
				<input type="email" name="email" autocomplete="off" id="email" placeholder="enter your email">
			</div>	
			<div id="product_key_div">
			<div class="input-box-pass">
				<input type="text" name="product" autocomplete="off" onkeyup="check_key()" id="product_key" placeholder="Enter the product key assigned">
			</div>
			<a href="loginpage.php" class="btn">Go Back to login page</a>
				</div>
				<div class="reset_password_form" id="reset_password_form">
					
						<div class="input-box-pass">
						<i class="fa fa-key"></i>
					<input type="password" name="new_password" id="new_password" placeholder="enter your new password">
				</div>
					<input type="submit" name="reset" value="submit" class="login-btn-pass">
					</form>
					<a href="loginpage.php" class="btn">Go Back</a>
				</div>
			</div>
		</div>
		
	</div>
	<script type="text/javascript">
		function show(){
			var x = document.getElementById("pass");
			var y = document.getElementById("hide1");
			var z = document.getElementById("hide2");
			if (x.type === 'password') {
				x.type = "text";
				y.style.display = "block";
				z.style.display = "none";
			}
			else{
				x.type = "password";
				y.style.display = "none";
				z.style.display = "block";
			}
		}

		function check_key(){
			var key = document.getElementById("product_key").value;
			var original_key = "amafhh786";
			if (key == original_key) {
				swal('success!', 'enter your new password','success');
				document.getElementById("reset_password_form").style.display="block";
				document.getElementById("product_key_div").style.display="none";
				}
			else if (key.length == original_key.length) {
					swal('OOPS!', 'wrong product key','error');
				
				}
			
		}
	</script>

</body>
</html>