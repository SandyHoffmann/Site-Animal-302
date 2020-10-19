$(function(){ 
    
    $.ajax({
        url: 'http://localhost:5000/listar_animal',
        method: 'GET',
        dataType: 'json', 
        success: listar_animal, 
        error: function() {
            alert("Deu erro");
        }
    });

    function listar_animal(animal) {
        
        for (var i in animal) { 
            if (animal[i].conteudo){
                conteudo = animal[i].conteudo
            }
            else{
                conteudo = ' Não há o que mostrar aqui :3 '
            }
            lin ='<div class="col-md-auto-p-0 border border" id="tabela"style="background-color: #A39BE8;outline-style: double; outline-color: white; ">'+
                '<h5 style="padding: 5px;"class="rounded">'+animal[i].nome_animal+'</h5>'+
                '<div class="row " >'+
                    '<div class="col-md-auto" style="background-color: #CAABFF;">'+
                    '<img src="image/logo.png" style="width: 200px;">'+
                    '</div>'+
                    '<div class="col" style="background-color: #ABE5FF"; id="conteudo">'+   
                    '<p>'+conteudo+'</p>'+   
                    '</div>'+
                    '<div class="col" style="background-color: #9BBCE8;">'+
                    '<div class="row">'+
                    '</div>'+
                    '<div class="col-p-0">'+
                    '<div class="row" style="background-color: #B8C4FF;margin-bottom: 0px;padding:10px;">'+
                        '<p>Família Cíentifica</p>'+
                        '<div class="row-md-auto">'+
                            '<p> - ' + animal[i].familia + '</p>' +
                        '</div>' +
                    '</div>'+
                    '<div class="row" style="margin-bottom: 0px;padding:10px;">'+
                        '<p>Habitat</p>'+
                        '<div class="row-md-auto">'+
                        '<p> - ' + animal[i].habitat + '</p>' +
                    '</div>' +
                    '</div>'+
                    '<div class="row" style="background-color: #B8C4FF;margin-bottom: 0px;padding:10px;">'+
                        '<p> Altura Média</p>'+
                        '<div class="row-md-auto">'+
                        '<p> - ' + animal[i].altura_media + ' metros.</p>' +
                    '</div>' +
                    '</div>'+
                    '<div class="row" style="margin-bottom: 0px;padding:10px;">'+
                        '<p>Peso Médio</p>'+
                        '<div class="row-md-auto">'+
                        '<p> - ' + animal[i].peso_medio + ' kilos.</p>' +
                    '</div>' +
                    '<div class="row" style="margin-bottom: 0px;padding:10px;">'+
                    '<div class="row-md-auto">'+
                    '<a href=# id="excluir_' + animal[i].id + '"'+'class="excluir_animal">Delete</a>' +
                '</div>' +
                    '</div>'+
                '</div>'+
            '</div>'+
            '</div>'+
            '</div>'+
            '</div>'+
            '<br>'
            $('#familiaver').append(lin);
        };
    };

$("#incluir_animal").click(function(){

    nome_animal = $("#nome_animal").val();
    familia = $("#familia").val();
    altura_media = $("#altura_media").val();
    peso_medio = $("#peso_medio").val();
    habitat = $("#habitat").val();
    conteudo = $("#conteudo").val();
    imagem_postagem = $("#imagem_postagem").val();

    dados = JSON.stringify({nome_animal:nome_animal, familia:familia,
        altura_media:altura_media, peso_medio:peso_medio,
        habitat:habitat,
        conteudo:conteudo, imagem_postagem:imagem_postagem});

    $.ajax({
        url: 'http://localhost:5000/incluir_animal',
        method: 'POST',
        contentType: 'application/json', 
        dataType: 'json',
        data: dados,
        success: incluir_animal, 
        error: erroincluir_animal
    });

    function incluir_animal(resposta){
        alert(resposta.detalhes);
        if (resposta.resultado == 'bele'){
            alert('Parabens, você cadastrou um novo animal! ');
            $("#nome_animal").val("");
            $("#familia").val("");
            $("#altura_media").val("");
            $("#peso_medio").val("");
            $("#habitat").val("");
            $("#conteudo").val("");
            $("#imagem_postagem").val("");

        }
        else{
            alert('Algo não correu bem, tente novamente :p');
        }
    }
    
    function erroincluir_animal(resposta){
        alert('Algo não correu bem, deuruim :p');
    }
    
});

$(document).on("click",".excluir_animal",function(){

    var clicado = $(this).attr('id');
    var nome = "excluir_";
    var id_animal = clicado.substring(nome.length);

    $.ajax({
        url: 'http://localhost:5000/excluir_animal/'+id_animal,
        type: 'DELETE',
        dataType: 'json',
        success: animalExcluido, 
        error: erroAoExcluir    
    });

    function animalExcluido(resposta){
        if (resposta.resultado == 'bele'){
            alert("Animal exluido com sucesso!");
        }
        else{
            alert(resposta.detalhes);
        }
    }
    function erroAoExcluir(resposta){
        alert("Erro ao excluir"+resposta.detalhes);
    }
});
}); 
