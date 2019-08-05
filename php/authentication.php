<?php
session_start();
include('db_config.php');
if(isset($_POST['Login']))
	{
		$email=$_POST['email'];
		$password=md5($_POST['password']);
		echo "$email <br> $password<br>";
		$query="SELECT * from registered_users WHERE email='$email' && password='$password'";
	    $result=mysqli_query($conn,$query);
	    $res=mysqli_fetch_assoc($result); 
	    $name=$res['name'];

	    $rowcount=mysqli_num_rows($result);
	    if ($rowcount==1) {
	    	$_SESSION['user'] = $name;
	    	
	    	header('location:../html/welcome_page.php');
	    }
	    else{
	    	echo "invalid username or password";
	    	header('location:../html/loginpage.php?id=invalid');
	    }
	}
if (isset($_POST['reset'])) {
	$email = $_POST['email'];
	$password = md5($_POST['new_password']);
	$query = "UPDATE registered_users set password = '$password' where email = '$email'";
	$result = mysqli_query($conn,$query);
	if ($result) {
	 	$_SESSION['password_reset'] = "True";
	 	header('location:../html/loginpage.php');
	 } 
}
?>
