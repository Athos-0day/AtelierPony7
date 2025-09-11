<?php
if(isset($_FILES['file'])){
    $file_name = $_FILES['file']['name'];
    $file_tmp = $_FILES['file']['tmp_name'];
    // ⚠️ aucune vérification sur l'extension ni le type du fichier
    move_uploaded_file($file_tmp,"upload/".$file_name);
    echo "Fichier uploadé : " . $file_name;
}
?>
<html>
<body>
    <h2>Upload de fichiers</h2>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="file"/>
        <input type="submit"/>
    </form>
</body>
</html>
