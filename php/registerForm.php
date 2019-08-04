<?php
$conn = mysqli_connect("127.0.0.1","root","", 'intp_project') or die(mysqli_error());
  if (!$conn) {
    echo "error connecting to mysql\n";
	echo " does'nt connected to database\n";
	}
if(isset($_POST['submit']))
	{ 

	$fname=$_POST['fname'];
	$nick=$_POST['nickname'];
	$number=$_POST['Number'];
	$Shopname=$_POST['shopname'];
  $shopAdd=$_POST['ShopAdd'];
	$email=$_POST['email'];
	$password=md5($_POST['password']);
  $gender=$_POST['gender'];
  $key=$_POST['product'];

  $query="INSERT INTO new_registration (fname,nickname,Number,shopname,ShopAdd,email,password,gender,product) VALUES ('$fname','$nick','$number','$Shopname','$shopAdd','$email','$password','$gender','$key')";
  echo "<br> $query";
  echo "<br>$fname<br> $nick<br> $number<br> $Shopname<br> $shopAdd<br> $email<br> $password<br> $gender<br> $key<br>";
    if(mysqli_query($conn,$query) == TRUE)
        {
          echo "INSERT Successful";
          header('location:loginpage.php');
   	    }
   	else
   	    {
   		   echo"error: ".$query."<br>". mysqli_error($conn);
        }
	  } 
else 
	{
	echo "values not received";
	}
?>