<html>
    <body>
        <script type="text/javascript">
            function val()
            {
                let a=document.getElementById("uname").value;
                var b=document.f1.password.value;
                if(a==="" && b==="")
                {
                    alert("enter username and password");
                }
                else if(a==="")
                {
                    alert("enter username");
                }
                else if(b==="")
                {
                    alert("enter password");
                }
                else{
                    
                }
            }
            </script>
        <center>
        <h1>login form</h1>
        <form method="POST" name="f1">
            <input type="text" name="uname" id="uname" placeholder="username"><br><br>
            <input type="password" name="password" id="password" placeholder="password"><br><br>
            <input type="submit" name="submit" id="submit" value="submit" onclick="val()"><br>
        </form>
        </center>
            
    </body>
</html>
<?php
    if(isset($_POST['submit']))
    {
    $conn = new mysqli("localhost","root","");
    $create="create database if not exists login";
    $a=$conn->query($create);
    $conn->close();
    $conn = new mysqli("localhost","root","","login");
    $table="create table if not exists login(username varchar(20) primary key,password varchar(20))";
    $conn->query($table);
    $u=$_POST['uname'];
    $p=$_POST['password'];
    if($u!='' and $p!=""){
    $q="select * from login where username='$u' and password='$p'";
    $result=$conn->query($q);
    if($result->num_rows>0){
     ?>
        <script>
            window.location="https://www.youtube.com/";
        </script>
    <?php
    }else{
        echo'Enter valid username and password';
    }
    }
    }
    
?>

