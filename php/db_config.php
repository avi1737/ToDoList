<?php
$conn = mysqli_connect("127.0.0.1","root","", 'medihelp') or die(mysqli_error());
  if (!$conn) {
    echo "error connecting to mysql\n";
	echo " does'nt connected to database\n";
	}
?>