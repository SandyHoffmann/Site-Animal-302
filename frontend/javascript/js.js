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
                    '<img src="../backend/'+animal[i].imagem_postagem+'" style="width: 200px;">'+
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
                    '</div>'+
                    '<div class="row" style="background-color: #B8C4FF;margin-bottom: 0px;padding:10px;">'+
                    '<a href=# id="excluir_' + animal[i].id + '"'+'class="excluir_animal" style="color: red;"><p><b>Delete</b></p></a>' +
                    '</div>'+
            '</div>'+
            '</div>'+
            '</div>'+
            '<div class="accordion" id="accordionExample">'+
                '<div class="card"style="background-color: #ffccff;">'+
                    '<div class="card-header" id="headingOne">'+
                    '<h5 class="mb-0">'+
                        '<button class="btn btn-link" type="button" style="background-color: #ff99c2;" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">'+'Zoológico '+animal[i].zoologicoanimal.nome_zoologico+'</button>'+
                    '</h5>'+
                    '</div>'+
                    '<div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">'+
                    '<div class="card-body">'+ '<p> - Endereço: ' + animal[i].zoologicoanimal.endereco +'</p>'+
                                                '<p> - Numero do Habitat: ' + animal[i].zoologicoanimal.numero_de_habitat + '</p>'+'</div>'+
                    '</div>'+
                '</div>'+
                '<div class="accordion" id="accordionExample">'+
                '<div class="card" style="background-color: #ccb3ff;">'+
                    '<div class="card-header" id="headingOne">'+
                    '<h5 class="mb-0">'+
                        '<button class="btn btn-link" type="button" style="background-color: #ff99c2;" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">'+'Cuidadores </button>'+
                    '</h5>'+
                    '</div>'+
                    '<div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">'+
                    '<div class="card-body">'+ '<p> - Nome do cuidador: ' + animal[i].cuidadores.nome_cuidador +'</p>'+
                                                '<p> - Especialidade: ' + animal[i].cuidadores.especialidade + '</p>'+
                                                '<p> - Idade: ' + animal[i].cuidadores.idade + '</p>'+'</div>'+
                    '</div>'+
                '</div>'+
            '</div>'+
            '<br>'
            $('#familiaver').append(lin);
        };
    };

//$("#incluir_animal").click(function()


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
            location.reload();
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

const registrar_ani = async() => {

    nome_animal = $("#nome_animal").val();
    familia = $("#familia").val();
    altura_media = $("#altura_media").val();
    peso_medio = $("#peso_medio").val();
    habitat = $("#habitat").val();
    conteudo = $("#conteudo").val();

    var img_file = document.getElementById("imagem_postagem").files[0];
    if (img_file != undefined){
        //Converte o BLOB em Base64 para passar por Json 
        imagem_postagem = await readFile(img_file);
    }
    else{
        imagem_postagem = null;
    };

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
    
};

function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $('#imagem_postagem')
          .attr('src', e.target.result)
          .width(200)
          .height(200);
      };
      reader.readAsDataURL(input.files[0]);
    }
};


//Ler a imagem adicionada pelo usuário e converter em base64
async function readFile(file_img) {

    return new Promise((resolve, reject) => {
        reader = new FileReader();

        reader.onload = () => {
            let base64 = (reader.result.split(",")[1]);
            resolve(base64);
        };

        reader.readAsDataURL(file_img);
    
    });

};
