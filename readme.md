 <img alt="GitHub language count" src="https://img.shields.io/badge/python-v3.7-purple"><img alt="GitHub language count" src="https://img.shields.io/badge/flask-v1.1.1-purple"><img alt="GitHub language count" src="https://img.shields.io/badge/Code-Open%20Source-purple">
<h1>Site Animal</h1>

Esse projeto tem como motivação fazer um site que possa cadastrar, listar e excluir dados para um trabalho escolar, utilizando python, javascript e html.

## 😺 Em que consiste o site?

O site de Animais consiste em uma página web onde se pode cadastrar animais juntamente de seu zoologico e de seu cuidador. tambem podendo excluir os mesmos. O site se encontra online no momento no site pythonanywhere podendo ser acessado no link abaixo.

* :star: <p><a href="http://sandyhoffmann.pythonanywhere.com/html/home.html">Clique para acessar o Site Animal</a></p>

O funcionamento do site ocorre com a utilização das bibliotecas Python SQLAlchemy  e Flask, com o auxilio do js.

![image]()
<i>Foto da home do website</i>

Tem-se então um servidor rodando a aplicação, por meio de rotas que desencadeiam as funcionalidades do site:

~~~python

#Rota para listar as salas, conversando com o JS
@app.route("/listar_animal")
def animais():
    animais = db.session.query(Animal).all()
    animaisjs = [ x.json() for x in animais ]
    manda = jsonify(animaisjs)
    manda.headers.add("Access-Control-Allow-Origin", "*") 
    return manda

~~~
<i>Exemplo de Rota, encontrada no backend.py</i>

Há tambem a persistência de dados, que ficam registrados no banco de dados intitulado como animal.db.
A criação de Tabelas desse bd é feita por meio do SqlAlchemy, que utiliza da classe Model.

~~~python

#Classe Zoologico
class Zoologico(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome_zoologico = db.Column(db.String(40), nullable = False)
    endereco = db.Column(db.String(40), nullable = False)
    numero_de_habitat = db.Column(db.Float, nullable = False)
    def __str__(self):
        return self.id+ str(self.nome_zoologico)+", "+self.endereco+", "+str(self.numero_de_habitat)
    
    def json(self):
        return {
            "id": self.id,
            "nome_zoologico": self.nome_zoologico,
            "endereco": self.endereco,
            "numero_de_habitat": self.numero_de_habitat
        }
~~~
<i>Exemplo de Tabela, encontrada no model.py</i>

E por fim, para auxiliar a conexão entre as páginas html e o backend (em python), tem-se o js, que chama as rotas, pega os dados, e encaminha para o html.

~~~python
  
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
~~~
<i>Exemplo de função de js, encontrada no js.js</i>

### 💻 Separação de Camadas

O site é dividido em backend (que possui as configurações, o servidor routes e o model) e em frontend (as páginas html, e o arquivo js).

### 📋 Como Executar o Programa

Para executar o programa é necessário ter a linguagem python instalada no computador, e executar o requirements.txt.
Rode o Backend e o servidor é para estar funcionando.

Se prefirir prefirir pode acessar online pelo <p><a href="http://sandyhoffmann.pythonanywhere.com/html/home.html">Site Animal</a></p>

```
Flask
SQLAlchemy
Bcrypt
Flask-LoginManager
Mail
Pillow
```
<i>Trecho do requirements.txt</i>


## 🛠️ Construído com

* [Pyhon](https://www.python.org/) - Python
* [js](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) - Javascript

## ✒️ Autora

* **Sandy Hoffmann** - *Programação* - [Sandy Hoffmann](https://github.com/SandyHoffmann)

## 📄 Licença

Este projeto está sob a licença de Código Aberto.
