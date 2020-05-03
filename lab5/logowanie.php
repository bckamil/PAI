<?php
require("funkcje.php");
require("index.php");

if (isSet($_POST['zaloguj'])) {
  echo "Przesłany login: " . test_input($_POST['login']) ."<br>";
  echo "Przesłane haslo: " . test_input($_POST['haslo']);

  if (test_input($_POST['login']) == $osoba1->login && test_input($_POST['haslo'])  == $osoba1->haslo) {
    $_SESSION["zalogowanyImie"] = $osoba1->imieNazwisko;
    $_SESSION["zalogowany"] = 1;
    header("Location: user.php");
  }
  if (test_input($_POST['login']) == $osoba2->login && test_input($_POST['haslo'])  == $osoba2->haslo) {
    $_SESSION["zalogowanyImie"] = $osoba2->imieNazwisko;
    $_SESSION["zalogowany"] = 1;
    header("Location: user.php");
  }
}
?>