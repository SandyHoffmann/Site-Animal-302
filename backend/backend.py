from config import *
from PIL import Image
import base64
import os, io
import secrets

@app.route("/listar_animal")
def animais():
    animais = db.session.query(Animal).all()
    animaisjs = [ x.json() for x in animais ]
    manda = jsonify(animaisjs)
    manda.headers.add("Access-Control-Allow-Origin", "*") 
    return manda

@app.route('/incluir_animal',methods=['post'])
def incluir_animal():
    resposta=jsonify({"resultado": "bele", "detalhes": "supimpa, vc conseguiu"})
    dados=request.get_json(force=True)
    animal_repetido = Animal.query.filter_by(nome_animal=dados['nome_animal'].capitalize()).first()
    if animal_repetido:
        resposta = jsonify({"resultado":"erro", "detalhes":"Animal com nome repetido"})
    else: 
        try:
            novo_animal=Animal(**dados)
            if (dados["imagem_postagem"] != None):
                novo_animal.imagem_postagem=salvar_imagem_base64('/imagens',(dados["imagem_postagem"]))
            db.session.add(novo_animal)
            db.session.commit()
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
    
def salvar_imagem_base64(diretorio, base64str):
    rhex = secrets.token_hex(9)
    nome_foto = rhex + ".png"
    nome_foto='imagens/'+nome_foto
    caminho = os.path.join(app.root_path, nome_foto )
    print(caminho)
    tamanho_imagem = (200, 200)
    
    image = base64.b64decode(str(base64str)) 
    
    imagem_menor = Image.open(io.BytesIO(image))
    imagem_menor.thumbnail(tamanho_imagem)
    imagem_menor.save(caminho)
    
    return nome_foto

    
@app.route('/excluir_animal/<int:animal_id>',methods=['DELETE'])
def excluir_animal(animal_id):
    resposta=jsonify({"resultado": "bele", "detalhes": "supimpa, vc conseguiu"})

    try:
        animal = Animal.query.get_or_404(animal_id)
        apagar_imagem(animal.imagem_postagem)
        db.session.delete(animal)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

def apagar_imagem(foto):
    if (foto != "imagens/logo.png"):
        caminho = os.path.join(app.root_path, foto)
        os.remove(caminho)
app.run(debug=True)



"""
from config import *

@app.route("/",methods=['GET','POST'])
def home():
    return render_template('template/base.html', titulo='AnimeWebSite')

@app.route("/listar_animal")
def animais():
    animais = db.session.query(Animal).all()
    animaisjs = [ x.json() for x in animais ]
    manda = jsonify(animaisjs)
    manda.headers.add("Access-Control-Allow-Origin", "*") 
    return manda

@app.route('/incluir_animal',methods=['post'])
def incluir_animal():
    resposta=jsonify({"resultado": "bele", "detalhes": "supimpa, vc conseguiu"})
    dados=request.get_json()
    try:
        novo_animal=Animal(**dados)
        db.session.add(novo_animal)
        db.session_commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

    dados=request.get_json()
    if not dados:
        print("alo")
    novo_animal=Animal(**dados)
    db.session.add(novo_animal)
    db.session.commit()
    resposta = jsonify({"resultado":"bele"}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

app.run(debug=True)
"""