<!DOCTYPE html>
<html>
<head>
	    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

	<!--<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>-->
	<link rel="stylesheet" type="text/css" href="../css/medicine_info.css">
	<title></title>

<script type="text/javascript">
//auto expand textarea
function adjust_textarea(h) {
    h.style.height = "20px";
    h.style.height = (h.scrollHeight)+"px";
}
</script>

<?php
include("../php/db_config.php");

$sql = "SHOW COLUMNS FROM medicine_info ";
$result = mysqli_query($conn,$sql);

$row = mysqli_fetch_array($result);

if (isset($_POST['submit'])) {
	

$medicine_name = $_POST['medicine_name'] ;
$Company_Name = $_POST['Company_Name'] ;
$Packaging_of_Product = $_POST['Packaging_of_Product'] ;
$Compositions = $_POST['Compositions'] ;
$Type_Of_Medicine= $_POST['Type_Of_Medicine'] ;
$Alchohol_Interaction = $_POST['Alchohol_Interaction'] ;
$Pregnancy_Interaction = $_POST['Pregnancy_Interaction'] ;
$Lactation_Interaction = $_POST['Lactation_Interaction'] ;
$uses = $_POST['uses'] ;
$Dosage = $_POST['Dosage'] ;
$Common_Side_Effect = $_POST['Common_Side_Effect'] ;

$insert_query = "INSERT INTO medicine_info (medicine_name ,Company_Name, Packaging_of_Product,
							Compositions,Type_Of_Medicine,Alchohol_Interaction,Pregnancy_Interaction,Lactation_Interaction,uses,Dosage,Common_Side_Effect) VALUES ('$medicine_name' ,'$Company_Name' , '$Packaging_of_Product',
							'$Compositions','$Type_Of_Medicine','$Alchohol_Interaction','$Pregnancy_Interaction','$Lactation_Interaction','$uses','$Dosage','$Common_Side_Effect')";


if (mysqli_query($conn,$insert_query)) {
	
	echo '<script type="text/javascript">';
    echo "swal('Congrats', 'medicine information entered ','success');";
    echo '</script>';
}
else{
	
	echo '<script type="text/javascript">';
    echo "swal('ERROR OCCURED', 'Contact DEVELOPER','error');";
    echo '</script>';
}


}
?>
</head>
<body>


	<div class="form-style-8">
  <h2>Enter Medicine Details.. </h2>
  <form method="POST" action="<?php echo($_SERVER['PHP_SELF']); ?>">
<?php
while($row = mysqli_fetch_array($result)){
    ?>
	<?php
	if ($row['Field'] == "id" ) {
		# do nothing
	}
	else {
	?>
    <input type="text" name="<?php echo $row['Field']; ?>" onkeyup="adjust_textarea(this)" placeholder="Enter <?php echo $row['Field']; ?>" />
    <?php
}
}
	?>
	<input type="submit" name="submit" value="submit">
  </form>
</div>


</body>
</html>