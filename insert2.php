<?php
if (isset($_POST["submit"]))
{
    if($_POST["qty1"]!=''){
        $p1=$_POST["qty1"];
    }else{
        $p1=0;
    }
    if($_POST["qty2"]!=''){
        $p2=$_POST["qty2"];
    }else{
        $p2=0;
    }
    if($_POST["qty3"]!=''){
        $p3=$_POST["qty3"];
    }else{
        $p3=0;
    }
    $sum=($p1*500)+($p2*100)+($p3*50);
    
}

?>
<center>
<h1>BILL</h1>
<table border="1">
     <tr>
            <th>id</th>
            <th>product</th>
            <th>price</th>
            <th>qty</th>
            <th>amount</th>
            </tr>
            <tr>
            <td>1</td>
            <td>bag</td>
            <td>500</td>
            <td><?php echo $p1; ?></td>
            <td><?php echo $p1*500; ?></td>
            </tr>
            <tr>
            <td>2</td>
            <td>book</td>
            <td>100</td>
            <td><?php echo $p2; ?></td>
            <td><?php  echo $p2*100; ?></td>
            </tr>
            <tr>
            <td>3</td>
            <td>pen</td>
            <td>50</td>
            <td><?php echo $p3; ?></td>
            <td><?php echo $p3*50; ?></td>
            </tr>
            <tr>
                <th colspan="5">total <?php echo $sum; ?></th>
            </tr>
</table>
</center>

