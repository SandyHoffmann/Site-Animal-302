from config import *
app = Flask(__name__) 
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'animal.db') 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+arquivobd 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome_animal = db.Column(db.String(40), nullable = False)
    familia = db.Column(db.String(40), nullable = False)
    altura_media = db.Column(db.Float, nullable = False)
    peso_medio = db.Column(db.Float, nullable = False)
    habitat = db.Column(db.String(40), nullable = False)
    data_postada = db.Column(db.DateTime, nullable = True)
    conteudo = db.Column(db.Text,nullable = False)
    imagem_postagem = db.Column(db.String(40), nullable = True)
    def __str__(self):
        return str(self.nome_animal)+" ,"+self.familia+" ,"+ self.altura_media +" ,"+self.peso_medio+" ,"+self.habitat+" ,"+self.conteudo+" ,"+self.imagem_postagem+","+self.data_postada
    
    def json(self):
        return {
            "id": self.id,
            "nome_animal": self.nome_animal,
            "familia": self.familia,
            "altura_media": self.altura_media,
            "peso_medio": self.peso_medio,
            "habitat": self.habitat,
            "data_postada": self.data_postada,
            "conteudo": self.conteudo,
            "imagem_postagem": self.imagem_postagem
        }
        
if __name__ == "__main__":
    db.create_all()
    novo = Animal(nome_animal = "cachorro",familia = 'Canis Lupus',altura_media = 90,peso_medio = 6,habitat = 'cidade',conteudo = 'cachorro tradicional',imagem_postagem = None, data_postada=None)
    novo2 = Animal(nome_animal = "gato",familia = 'Felix Cat',altura_media = 60,peso_medio = 4,habitat = 'cidade',conteudo = 'miau miau miau',imagem_postagem = None, data_postada=None)
    db.session.add(novo)
    db.session.add(novo2)
    db.session.commit()
