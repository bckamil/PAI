<?php session_start(); ?>
<!DOCTYPE html>
<html>

<head>
  <title>PHP</title>
  <meta charset='UTF-8' />
</head>

<body>
  <?php
    echo "<h3>Nasz system</h3>";
  ?>
  <form action="logowanie.php" method="POST">
    <fieldset>
      <legend>Logowanie:</legend>
      <label for="login">Login:</label>
      <input type="text" id="login" name="login">
      <br>
      <label for="haslo">Haslo:</label>
      <input type="password" id="haslo" name="haslo">
      <br>
      <button type="submit" name="zaloguj">Zaloguj</button>
    </fieldset>
  </form>

  <hr />
  <form action="cookie.php" method="GET">
    <fieldset>
      <legend>Cookie:</legend>
      <label for="czas">Czas:</label>
      <input type="text" name="czas" id="czas">
      <button type="submit" name="utworzCookie">utworzCookie</button>
    </fieldset>
  </form>
</body>

</html>

<?php
if (isSet($_POST["wyloguj"])) {
  $_SESSION["zalogowany"] = 0;
}

if (isSet($_COOKIE["nazwa"])) {
  echo $_COOKIE["nazwa"];
}
?>