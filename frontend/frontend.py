"""
from config import *
from flask import request, requests
from model import Animal

@app.route("/listar_animal") 
def listar_animal(): 
   resultado_requisicao = requests.get('http://localhost:5000/listar_animal') 
   json_animal = resultado_requisicao.json() 
   animal_em_python = [] 
   for a in json_animal: 
      an = Animal(**a) 
      animais_em_python.append(an) 
 
   return render_template("listar_animal.html", listagem = animal_em_python) 

app.run(debug=True, port=4999)
"""