<!DOCTYPE html>
<html>
<head>
	<title>Registration Page</title>
  <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
  <?php
  if (isset($_SESSION['email_taken'])) {
    if ($_SESSION['email_taken'] == "True") {
      echo '<script type="text/javascript">';
      echo "swal('congrats!', 'your password has changed','success');";
      echo '</script>';
    }
  }
  ?>
	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="../css/StyleRegister.css">
</head>
<body>
    <h1>New User Sign-Up</h1>
    <div class="register">
        <div class="form">
        <h2>Fill-up your details </h2>
        <form method="post" id="register" action="../php/registerForm.php">    
        <table  cellpadding="10px" >
        	
        	<tr>     		
         		<td><label>Full Name : </label></td>
         		<td><input type="text" name="name" placeholder="Enter your full name" id="fullname" autofocus required></td>
            </tr>            
            <tr>
         		<td><label>Contact Number : </label></td>
         		<td><select id="ph">
         			<option>+ 91</option>
         			<option>+ 022</option>
         			<option>+ 93</option>
         			<option>+ 92</option>
         			<option>+ 199</option>
         		</select>
         		<input type="Number" name="Number" placeholder="Enter your 10 digit mobile number" id="Phone" onchange="return validateNumber()" required><span id="star"></span><p id="phone" ></p> </td>
            </tr>
            
            <tr>
         		<td><label>Shop Name : </label></td>
         		<td><input type="text" name="shopname" placeholder="Enter your Shop Name" id="shopname" required></td>
         	</tr> 
         	
         	<tr>
         		<td><label>Shop Address : </label></td>
         		<td><input type="text" name="ShopAdd" placeholder="Enter your shop address" id="Shopadd" required></td>
         	</tr>
         	
         	<tr>
         		<td><label>Email Address : </label></td>
         		<td><input type="email" name="email" placeholder="example@gmail.com" id="email" onfocusout="return validateEmail()" required><span id="star1"></span><p id="EMAIL"></p></td>
         	</tr>
			
			<!--<tr>
         		<td><label>Password : </label></td>
         		<td><input type="password" name="password" placeholder="Enter your password" id="password" required> <button id="showPassword" onclick="return Toggle()"></button></td>
         	</tr>-->

         	<tr>
         		<td><label>Password : </label></td>
         		<td><input type="password" name="password" placeholder="Enter your password" id="password" required><span class="eye" onclick="return show()" id="show">
				<i id="hide2" class="fa fa-eye-slash"></i>
				<i id="hide1" class="fa fa-eye"></i>
			</span></td>
         	</tr>
			
			<tr>
         		<td><label>Re-enter Password : </label></td>
         		<td><input type="password" name="password" placeholder="Re-enter your password again" id="pass" onchange="return Validate()" required><!--<span class="eye" onclick="return show()" id="show">
				<i id="hide2" class="fa fa-eye-slash"></i>
				<i id="hide1" class="fa fa-eye"></i>
			</span>--><span id="star2"></span><p id="spam"></p></td>
            </tr>
			
			<tr>
         		<td><label>Product Key : </label></td>
         		<td><input type="text" name="product" placeholder="Enter the product key" id="product" onchange="return Validate()" required><span id="star3"></span><p id="invalidKey"></p></td>
            </tr>

            <tr>  
                <td colspan=2 align="center"><input type="submit" name="submit" value="Register" id="submit" onclick="return Validate()">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <input type="reset" name="cancel" value="Reset" id="reset"></td>
            </tr>
        </table>
        </form>
    	</div>
    </div>
    <script type="text/javascript">
       	function Validate() {
          	var password = document.getElementById("password").value;
            var confirmPassword = document.getElementById("pass").value;
            var key = document.getElementById("product").value;
            var original_key =  "amafhh786";
            if (key != original_key) {
              document.getElementById("invalidKey").innerHTML="Invalid Key";
              document.getElementById("product").style.borderColor = "red";
              document.getElementById("star3").innerHTML=" *";  
            }
            if (confirmPassword=="") {
          		document.getElementById("spam").innerHTML="confirm password field is empty";
           		document.getElementById("pass").style.borderColor = "red";
           		document.getElementById("star2").innerHTML=" *";
           		return false;
           	}
           	if (password != confirmPassword) {
               	//window.alert("Passwords do not match.");
               	document.getElementById("pass").style.borderColor = "red";
               	document.getElementById("spam").innerHTML="Passwords doesn't match";
               	document.getElementById("star2").innerHTML=" *";
               	return false;
               	}
           	else{
           		  document.getElementById("pass").style.borderColor = "black";
               	document.getElementById("spam").innerHTML="";
               	document.getElementById("star2").innerHTML="";
                document.getElementById("invalidKey").innerHTML="";
                document.getElementById("product").style.borderColor = "black";
           	}
        }
				
        function validateNumber() {
           	var phone = document.getElementById("Phone").value;
           	if (phone.length != 10) {
           		document.getElementById("phone").innerHTML="Enter valid phone number";
           		document.getElementById("Phone").style.borderColor="red";
                document.getElementById("star").innerHTML=" *";
                return false;
            }
            else{
            	document.getElementById("phone").innerHTML="";
            	document.getElementById("star").innerHTML="";
            	document.getElementById("Phone").style.borderColor="black";
            }
        }

		function validateEmail(){
			var email = document.getElementById("email").value;
			if(email.indexOf("@")<=0){
				document.getElementById("EMAIL").innerHTML="  Invalid Email Address";
				document.getElementById("email").style.borderColor = "red";
				//window.alert("Invalid Email Address");
				document.getElementById("star1").innerHTML=" *";
				return false;
			}
			if ((email.charAt(email.length-4)!=".") && (email.charAt(email.length-3)!=".")) {
				document.getElementById("EMAIL").innerHTML=" * Invalid Email Address";
				document.getElementById("email").style.borderColor = "red";
				document.getElementById("star1").innerHTML=" *";
				//window.alert("Invalid Email Address");
				return false;
			}
			else{
				document.getElementById("EMAIL").innerHTML="";
				document.getElementById("email").style.borderColor="black";	
				document.getElementById("star1").innerHTML=""
				} 
			/*		
			if (email.charAt(email.length-3)!=".") {
				document.getElementById("EMAIL").innerHTML=" ** Invalid Email Address"
				//window.alert("Invalid Email Address");
				return false;
			} */
			return true;
		} 

		function show(){
			var x = document.getElementById("password");
			var w = document.getElementById("pass");
			var y = document.getElementById("hide1");
			var z = document.getElementById("hide2");
			if (x.type === 'password' && w.type === 'password') {
				x.type = "text";
				w.type = "text";
				y.style.display = "block";
				z.style.display = "none";
			}
			else{
				x.type = "password";
				w.type = "password";
				y.style.display = "none";
				z.style.display = "block";
			}
		}
    </script>
</body>
</html>

