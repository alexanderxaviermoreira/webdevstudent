function showImgOne(){
    window.document.querySelector('.rightButton').addEventListener('click',()=>{
        window.document.querySelector('.img01').style.transform='translatex(-125px)';
        window.document.querySelector('.img02').style.transform='translatex(-125px)';
        window.document.querySelector('.discrTwo').style.display='block';
        window.document.querySelector('.discrOne').style.display='none';
    });
}
showImgOne();

function showImgTwo(){
    window.document.querySelector('.leftButton').addEventListener('click',()=>{
        window.document.querySelector('.img02').style.transform='translatex(125px)';
        window.document.querySelector('.img01').style.transform='translatex(125px)';
        window.document.querySelector('.discrOne').style.display='block';
        window.document.querySelector('.discrTwo').style.display='none';
    });
}
showImgTwo();