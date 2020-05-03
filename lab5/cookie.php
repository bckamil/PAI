<?php session_start(); ?>
<!DOCTYPE html>
<html>

<head>
  <title>PHP</title>
  <meta charset='UTF-8' />
</head>

<body>
  <?php
    echo "<p>Zalogowano</p>";

    echo "<span>" . $_SESSION["zalogowanyImie"] . "</span>";
  ?>
  
  <a href="index.php">Wstecz</a>

  <?php
  if (isset($_GET["utworzCookie"])) {
    setcookie("nazwa", "wartość", time() + $_GET["czas"], "/");
  }

  ?>
</body>

</html>