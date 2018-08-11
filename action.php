<html>
<body>

<h1>Your comment is logged.Thank you.</h1>

<?php

$file = fopen("log.txt","a") or die("ERROR");
fwrite($file,$_GET["name"]);
fwrite($file," : ");
fwrite($file,$_GET["comment"]);
fwrite($file,"\n");
fclose($file);

?>
  <p></p>
  <p>If you see this message,your file has been changed.</p>
</body>
</html>
