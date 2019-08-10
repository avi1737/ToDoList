<?php
session_start();

if(isset($_SESSION['user'])){
	unset($_SESSION['user']);
}

?>

<!DOCTYPE html>
<html>
<head>
	
	<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
	<?php
	if(!empty($_SESSION['password_reset'])){ 
		echo $_SESSION['password_reset'];
		if($_SESSION['password_reset'] == "True" ){
				echo '<script type="text/javascript">';
				echo "swal('congrats!', 'your password has changed','success');";
				echo '</script>';
			}
			unset($_SESSION['password_reset']);
		}	
		if(!empty($_SESSION['user_entry'])){
			if($_SESSION['user_entry'] == 'success'){
				echo '<script type="text/javascript">';
				echo "swal('Good job!', 'you have succesfully registered!','success');";
				echo '</script>';	
			}elseif($_SESSION['user_entry'] == 'invalid'){
				echo '<script type="text/javascript">';
				echo "swal('OOPS', 'INVALID EMAIL OR PASSWORD','error');";
				echo '</script>';
			}
			unset($_SESSION['user_entry']);
		}

		?>
	<title>login page</title>
	<link rel="stylesheet" type="text/css" href="../css/stylelogin.css">
	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
	<div class="form-box">
	<form method="post" action="../php/authentication.php">
	
		<h1>Login</h1>
		
		<div class="input-box">
			<i class="fa fa-envelope-o"></i>
			<input type="email" name="email" placeholder="email-id" id="email" autofocus>
		</div>
		<div class="input-box">
			<i class="fa fa-key"></i>
			<input type="password" name="password" placeholder="password" id="pass">
			<span class="eye" id="eye" onclick="return show()">
				<i id="hide2" class="fa fa-eye-slash"></i>
				<i id="hide1" class="fa fa-eye"></i>
			</span>
		</div>
		<input type="submit" class="login-btn" value="Login" name="Login">
		
		<a href="registerForm.php" class="btn" id="Register-btn">Register now</a>	
	<a href="reset_password_form.php" class="btn" id="forgotton-pass-btn" onclick="forgot_password()">Forgot your password ?</a>
</form>
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

	</script>
</body>
</html>