<?php

session_start();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

  <?php
  if (isset($_POST['submit'])) {

    $name = $_POST['name'];
    #$email = $_POST['email'];
    #$message = $_POST['message'];
    #$msg = "name : ".$name."\n Email : ".$email."\n\n message: ".$message;
    #$myemail = "syedrasique718@gmail.com";
    #$subject = "contact message from ".$email;
    #$mail =mail($myemail, $subject, $msg);
    echo $name;
    echo '<script type="text/javascript">';
    echo "swal('Congrats', 'your mail has been sent','success');";
    echo '</script>';
    }


  ?>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>MEDIHELP-India's Pharmacy Management APP</title>
    <link href="../css/landingPage.css" rel="stylesheet"></style>
    <link href="/your-path-to-fontawesome/css/all.css" rel="stylesheet">
</head>
<body>
   <nav id="nav">
       <div class="navbar-brand">
           <a href="#" id="logo">MEDIHELP</a>
       </div>
       <div class="nav-items">
           <ul>
               <li><a href="#" id="hover_bg">Home</a></li>
               <li><a href="#Services" id="hover_bg">Services</a>
              <?php
            if(isset($_SESSION['user'])){
              ?>
              <li><a href="#" id="hover_bg">Tools</a></li>
              <?php } ?>      
            	</li>
               <li><a href="#about" id="hover_bg">About Us</a></li>
               <li><a href="#contacts" id="hover_bg">Contact</a></li>
           </ul>
       </div>
       <div class="options">
        <div class="nav-items_sign_in">
        <?php
            if(isset($_SESSION['user'])){
          ?>
          
         <li><a href="loginpage.php"><?php echo $_SESSION['user'] ?>/Logout</a>
            </li>
          
        <?php }else{ ?>
           <a href="registerForm.php" >Sign Up</a>
           <a href="loginpage.php" >Log In</a>
         <?php } ?> 
       </div>
       </div>
   </nav>

   <div class="container">
      <h1><p id="welcome">Welcome</P> To India's Pharmacy Management App.</h1>
   </div>
   <div class="brand-name" id="Services">
        <h3>OUR APP SERVICES</h3>
   </div>
  
   <div class="brand-container">
       <div class="info-card">
        <div class="img-container">
        <img src="../images/bill.jpg" width="100%" height="30%">
        </div>
        <h2>Easy bill storage </h2>
        <button>Know More</button>
       </div>
       <div class="info-card">
        <div class="img-container">
        <img src="../images/register.jfif" width="100%" height="30%">
        </div>
        <h2>Manage your Stocks</h2>
        <button>Know More</button>
    </div>
    <div class="info-card">
        <div class="img-container">
        <img src="../images/register.jfif" width="100%" height="50%">
        </div>
        <h2>Sold items list</h2>
        <button>Know More</button>
    </div>
   </div>
  

   <div class="brand-container">
    <div class="info-card">
        <div class="img-container">
                <img src="../images/barcode.jpg" width="100%" height="220px">
         </div>
         <br/><h2>Barcode Based Selling</h2></br>
         <button>Know More</button>
 
    </div>
    <div class="info-card">
            <div class="img-container">
                    <img src="../images/profit.jpg" width="100%" height="220px">
             </div>
				
             <br/><h2>Daily and Monthly profit Chart</h2></br>
             <button>Know More</button>     
    
    </div>
    <div class="info-card">
            <div class="img-container">
                    <img src="../images/herbal.jpg" width="100%" height="220px">
             </div>

             <br/><h2>Medicine Tracking</h2></br>
             <button>Know More</button> 
    
    </div>
   </div>

   <div class="about-container" id="about">
       <h2>ABOUT US</h2>
       <p>MEDIHELP is not just an app but it's a vision of its Founder Mr. Husain Abbas to create something so easy that even person with no prior knowledge can use it and without the help of our Co-founders none of this would be possible.</p>
       <p>We are proud to complement the services of our local pharmacy through accurate and detailed information of their medicine. Our efficient team of Pharmacists and Developers strive to provide prompt and friendly service. Quality and accuracy are values we refuse to compromise.</p>
       <p>our Co-founders are </p>
       <ul>
           <li>Mr Ganesh Soni</li>
           <li>Mr Avinash Varpeti</li>
       </ul>
   </div>

   <div class="contact-container" id="contacts">
       <div class="contact-heading">
       <h1>Contact</h1>

       </div>
       <p>We would Love To Help You!</p>

       <div class="contact-form">
         <form id="forms" method="POST" action='<?php echo($_SERVER['PHP_SELF']); ?>'>
             <input type="text" name="name" placeholder="Your Name.." required>
             <input type="email" name="email" placeholder="Your Email.." required>
             <textarea name="message" form="forms" rows="5" cols="67" placeholder="Enter text here .."></textarea>

             <input type="submit" value="Submit" name="submit" id="submit-it">
         </form>
       </div>
       <div class="address">
        <p><b>Location:</b>  Dr. K. M. Vasudevan Pillai Campus, Plot No. 10, Sector 16, New Panvel, Navi Mumbai, Maharashtra 410206</p>
        <p><b>Phone:</b>8451895156</p>
        <p><b>Email:</b>contact@medihelp.in</p>
       </div>
   </div>


   <div class="footer">
       <p>© MediHelp.com, Inc. All rights reserved for 2019</p>
   </div>
   <script src="../js/landingPage.js"></script>
</body>
</html>