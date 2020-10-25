// Função para carregar a página antes de executar o jQuery
// jQuery ==> Evitar conflito com outra variável
jQuery(document).ready(function() {
    console.log("PÁGINA CARREGADA");
});
// Função para carregar a página antes de executar o jQuery

$(function(){
    $('.menu_hamburguer').bind('click', function(){
        $('.sobreMenu').animate({
            'left':0
        },500);
    });
    $('.fecharSobreMenu').bind('click', function(){
        $('.sobreMenu').animate({
            'left':-2000
        },500);
    });
});

