from config import *
from config import app
from config import db

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

class Cuidador(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome_cuidador = db.Column(db.String(40), nullable = False)
    especialidade = db.Column(db.String(40), nullable = False)
    idade = db.Column(db.Float, nullable = False)
    zoologicocuidadorid = db.Column(db.Integer,db.ForeignKey(Zoologico.id),nullable=False)
    zoologicocuidador = db.relationship("Zoologico")

    def __str__(self):
        return self.id+ str(self.nome_cuidador)+", "+self.especialidade+", "+str(self.idade)+", "+str(self.zoologicocuidadorid)+", "+self.zoologicocuidador
    
    def json(self):
        return {
            "id": self.id,
            "nome_cuidador": self.nome_cuidador,
            "especialidade": self.especialidade,
            "idade": self.idade,
            "zoologicocuidadorid": self.zoologicocuidadorid,
            "zoologicocuidador":self.zoologicocuidador.json()
        }
class Animal(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome_animal = db.Column(db.String(40), nullable = False)
    familia = db.Column(db.String(40), nullable = False)
    altura_media = db.Column(db.Float, nullable = False)
    peso_medio = db.Column(db.Float, nullable = False)
    habitat = db.Column(db.String(40), nullable = False)
    conteudo = db.Column(db.Text,nullable = False)
    imagem_postagem = db.Column(db.String(40), nullable = False, default='imagens/logo.png')
    cuidadorid = db.Column(db.Integer,db.ForeignKey(Cuidador.id),nullable=False)
    cuidadores = db.relationship("Cuidador")
    zoologicoanimalid = db.Column(db.Integer,db.ForeignKey(Zoologico.id),nullable=False)
    zoologicoanimal = db.relationship("Zoologico")
    
    def __str__(self):
        return self.id+ str(self.nome_animal)+" ,"+self.familia+" ,"+ self.altura_media +" ,"+self.peso_medio+" ,"+self.habitat+" ,"+self.conteudo+" ,"+self.imagem_postagem+" ,"+str(self.cuidadorid)+", "+self.cuidadores+", "+str(self.zoologicoanimalid)+", "+self.zoologicoanimal
    
    def json(self):
        return {
            "id": self.id,
            "nome_animal": self.nome_animal,
            "familia": self.familia,
            "altura_media": self.altura_media,
            "peso_medio": self.peso_medio,
            "habitat": self.habitat,
            "conteudo": self.conteudo,
            "imagem_postagem": self.imagem_postagem,
            "cuidadorid": self.cuidadorid,
            "cuidadores": self.cuidadores.json(),
            "zoologicoanimalid": self.zoologicoanimalid,
            "zoologicoanimal":self.zoologicoanimal.json()
        }
        

if __name__ == "__main__":
    cuidador1 = Cuidador(nome_cuidador = "José",especialidade = 'Veterinário',idade = 25, zoologicocuidadorid=1)
    db.session.add(cuidador1)
    db.session.commit()
    print(cuidador1.json())
    print(f"Cuidador: {cuidador1.json()}")

    cuidador2 = Cuidador(nome_cuidador = "Fabiana",especialidade = 'Veterinária',idade = 66, zoologicocuidadorid=2)
    db.session.add(cuidador2)
    db.session.commit()
    print(cuidador2.json())
    print(f"Cuidador: {cuidador2.json()}")

    cuidador3 = Cuidador(nome_cuidador = "Lampião",especialidade = 'Zoologo',idade = 33, zoologicocuidadorid=2)
    db.session.add(cuidador3)
    db.session.commit()
    print(cuidador3.json())
    print(f"Cuidador: {cuidador3.json()}")

    cuidador4 = Cuidador(nome_cuidador = "Marcela",especialidade = 'Biologa',idade = 23, zoologicocuidadorid=3)
    db.session.add(cuidador4)
    db.session.commit()
    print(cuidador4.json())
    print(f"Cuidador: {cuidador4.json()}")
    """
    novo = Animal(nome_animal = "cachorro",familia = 'Canis Lupus',altura_media = 90,peso_medio = 6,habitat = 'cidade',conteudo = 'cachorro tradicional',imagem_postagem = None)
    novo2 = Animal(nome_animal = "gato",familia = 'Felix Cat',altura_media = 60,peso_medio = 4,habitat = 'cidade',conteudo = 'miau miau miau',imagem_postagem = None)
    db.session.add(novo)
    db.session.add(novo2)
    db.session.commit()
    db.create_all()
    cuidador1 = Cuidador(nome_cuidador = "richard",especialidade = 'zoologo',idade = 15, zoologicocuidadorid=2)
    db.session.add(cuidador1)
    db.session.commit()
    print(cuidador1.json())
    print(f"Cuidador: {cuidador1.json()}")
    db.create_all()

    zoologico1 = Zoologico(nome_zoologico = "Animais Felizes",endereco = 'Pomerode',numero_de_habitat = 9)
    db.session.add(zoologico1)
    db.session.commit()
    print(zoologico1.json())

    cuidador1 = Cuidador(nome_cuidador = "José",especialidade = 'Veterinário',idade = 25, zoologicocuidador=zoologico1)
    db.session.add(cuidador1)
    db.session.commit()
    print(cuidador1.json())
    print(f"Cuidador: {cuidador1.json()}")

    animal = Animal(nome_animal = "gato",familia = "felix gatus",altura_media = 0.3, peso_medio=4, habitat="cidade", conteudo="miaumiau", cuidadorid=1,zoologicoanimalid=1)
    db.session.add(animal)
    db.session.commit()
    print(animal.json())

    zoologico1 = Zoologico(nome_zoologico = "Rave dos Carangueijo",endereco = 'Ilha dos Caribenhos',numero_de_habitat = 19)
    db.session.add(zoologico1)
    db.session.commit()
    print(zoologico1.json())

    zoologico1 = Zoologico(nome_zoologico = "Animais Felizes",endereco = 'Pomerode',numero_de_habitat = 9)
    db.session.add(zoologico1)
    db.session.commit()
    print(zoologico1.json())

    cuidador1 = Cuidador(nome_cuidador = "José",especialidade = 'Veterinário',idade = 25, zoologicocuidador=zoologico1)
    db.session.add(cuidador1)
    db.session.commit()
    print(cuidador1.json())
    print(f"Cuidador: {cuidador1.json()}")

    animal = Animal(nome_animal = "gato",familia = "felix gatus",altura_media = 0.3, peso_medio=4, habitat="cidade", conteudo="miaumiau", cuidadorid=1,zoologicoanimalid=1)
    db.session.add(animal)
    db.session.commit()
    print(animal.json())
-------------------------------------------------------------------------------
    zoologico1 = Zoologico(nome_zoologico = "Animais Felizes",endereco = 'Rua das Alamedas - Pomerode',numero_de_habitat = 9)
    db.session.add(zoologico1)
    db.session.commit()
    print(zoologico1.json())


    zoologico2 = Zoologico(nome_zoologico = "Ilha Fantasia",endereco = 'Rua Felipe de Carvalho - Ilha dos Caribenhos',numero_de_habitat = 19)
    db.session.add(zoologico2)
    db.session.commit()
    print(zoologico2.json())

    zoologico3 = Zoologico(nome_zoologico = "Selva Selvagem",endereco = 'Morro do Macaco - Indaial',numero_de_habitat = 66)
    db.session.add(zoologico3)
    db.session.commit()
    print(zoologico3.json())
"""