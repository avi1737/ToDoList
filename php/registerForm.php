<?php
session_start();

include('db_config.php');
if(isset($_POST['submit']))
	{ 

	$name=$_POST['name'];
	$number=$_POST['Number'];
	$Shopname=$_POST['shopname'];
  $shopAdd=$_POST['ShopAdd'];
	$email=$_POST['email'];
	$password=md5($_POST['password']);

/*        
    $registered_users = "SELECT Email from registered_users";
    $registered_email = mysqli_query($conn ,$registered_users);
    $Email = mysqli_fetch_assoc($registered_email);
    while($Email){
      if ($Email['Email']==$email) {
        $_SESSION['email_taken'] = "True";
        header('location:../html/registerForm.php?id=email_taken');
      }
    }

  */
    $query="INSERT INTO registered_users (name,mobile_number,shop_name,shop_address,Email,password) VALUES ('$name','$number','$Shopname','$shopAdd','$email','$password')";
        if(mysqli_query($conn,$query) == TRUE)
          {
            $_SESSION['user_entry'] = "success";
            header('location:../html/loginpage.php');
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

