from config import *
from flask import jsonify, request
from PIL import Image
import os,io
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
            db.session.add(novo_animal)
            db.session.commit()
        except Exception as e: 
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

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