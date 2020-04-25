<?php session_start(); ?>
<?php
print<<<KONIEC
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<form action="form06_redirect.php" method="POST">
id_prac <input type="text" name="id_prac">
nazwisko <input type="text" name="nazwisko">
<input type="submit" value="Wstaw">
<input type="reset" value="Wyczysc">
</form>
KONIEC;

if (isset($_SESSION["MYSQL_ERROR"])) {
    echo "Query failed: " . $_SESSION["MYSQL_ERROR"];
}
?>