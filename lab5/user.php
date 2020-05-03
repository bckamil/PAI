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
  <form action="index.php" method="POST">
    <button type="submit" name="wyloguj">Wyloguj</button>
  </form>
  <hr />
  <form action='user.php' method='POST' enctype='multipart/form-data'>
    <fieldset>
      <legend>Wyślij plik:</legend>
      <label for="file">Wybierz plik</label>
      <input type="file" name="file"><br>
      <button type="submit" name="upload">Wyślij</button>
    </fieldset>
  </form>
</body>

</html>

<?php
require("funkcje.php");

if ($_SESSION["zalogowany"] != 1) {
  echo $_SESSION["zalogowany"];
  header("Location: index.php");
}

if (isset($_POST['upload'])) {
  $fileName = $_FILES["file"]["name"];
  $fileType = $_FILES["file"]["type"];
  if ($fileType == 'image/png' or $fileType == 'image/jpeg'
    or $fileType == 'image/JPEG' or $fileType == 'image/PNG') {
    
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $fileName)) {
      echo "<img src=".$fileName." height=250 width=250 /><br>";
    } else {
      echo "<p>Wysątpił błąd<p>";
    }
  } else {
    echo "<p>Brak pliku o odpowiednim rozszerzeniu</p>";
  }
}
?>