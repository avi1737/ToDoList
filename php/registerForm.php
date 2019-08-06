<?php


include('db_config.php');
if(isset($_POST['submit']))
	{ 

	$name=$_POST['name'];
	$number=$_POST['Number'];
	$Shopname=$_POST['shopname'];
  $shopAdd=$_POST['ShopAdd'];
	$email=$_POST['email'];
	$password=md5($_POST['password']);
        
    $registered_users = "SELECT Email from registered_users";
    $registered_email = mysqli_query($conn ,$registered_users);
    if($email == $registered_users){

    }

    $query="INSERT INTO registered_users (name,mobile_number,shop_name,shop_address,Email,password) VALUES ('$name','$number','$Shopname','$shopAdd','$email','$password')";
        if(mysqli_query($conn,$query) == TRUE)
          {
            echo "INSERT Successful";
            header('location:../html/loginpage.php?id=registered_user');
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

