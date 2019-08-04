<?php
$conn = mysqli_connect("127.0.0.1","root","", 'intp_project') or die(mysqli_error());
  if (!$conn) {
    echo "error connecting to mysql\n";
	echo " does'nt connected to database\n";
	}
if(isset($_POST['Login']))
	{
		$email=$_POST['email'];
		$password=md5($_POST['password']);
		echo "$email <br> $password<br>";
		$query="SELECT * from new_registration WHERE email='$email' && password='$password'";
	    $result=mysqli_query($conn,$query); 
	    $rowcount=mysqli_num_rows($result);
	    if ($rowcount==True) {
	    	header('location:welcome.php');
	    }
	    else{
	    	echo "invalid username or password";
	    	header('location:loginpage.php');
	    }
	}
?>
