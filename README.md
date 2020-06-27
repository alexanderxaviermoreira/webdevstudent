<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
<style>
*{
    margin: 0; padding:0; border: 0; box-sizing: border-box;
    }
    body{
        width: 100%; min-height: 100vh;display: flex; flex-direction: column; justify-content: space-around; align-items: space-around;border: 5px solid #fff; padding: 15px; border-radius: 20px;
    }
    .topo{
display: flex; justify-content: center; width: 100%; padding: 10px
    }
    .topo img{
width: 200px; border-radius: 10px; box-shadow: 5px 5px 4px #212121; margin: 20px;
    }
    .title{
background-color:#ccc; display: flex; justify-content: center; align-items: center; padding: 10px; border-radius: 10px;
    }
.title a{
color: #212121;display: flex;justify-content: center;align-items: center; text-decoration: none;
}
    .horRule{
background-color:red; width: 100%; height: 5px; margin: 15px 0;
}
.subtitle{
font-family: monospace; font-weight: 100;text-align: center; margin: 20px 0;
}
.skills{
border-radius: 10px;padding: 5px;border: 3px solid;display: flex; align-items: center; justify-content: space-around;
}
.skills li{
    text-transform: uppercase; list-style: none; font-size: 20px; font-weight: bolder;
}
</style>

</head>
<body>

<header class="topo">
<img src="https://cdn.pixabay.com/photo/2018/09/08/22/37/software-3663509_960_720.jpg" alt="Imagem Gratuita - Web Developer">
</header>    

<h1 class="title">
    <a href="">Alexander Xavier Moreira</a>
</h1>

<hr class="horRule">

<h4 class="subtitle">Estudo de Desenvolvimeto Web</h4>

<div class="skills">
    <li>html</li>
    <li>css</li>
    <li>javascript</li>
    <li>php</li>
</div>

</body>
</html>