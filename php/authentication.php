<?php
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
	    	header('location:../html/welcome_page.php?id='.$name.'');
	    }
	    else{
	    	echo "invalid username or password";
	    	header('location:../html/loginpage.php?id=invalid');
	    }
	}
?>
