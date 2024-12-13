import json

class personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, oponente):
        oponente.vida -= self.ataque
        print(f"{self.nome} Ataca {oponente.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(personagem):
    def especial(self, oponente):
        dano = 30
        oponente.vida -= dano
        print(f"{self.nome} usa Golpe poderoso em {oponente.nome} e Causa {dano} de Dano!")

class Mago(personagem):
    def especial(self):
        cura = 25
        self.vida += cura
        print(f"{self.nome} usa Cura e Ganha {cura} Pontos de Vida!")

class Arqueiro(personagem):
    def especial(self, oponentes):
        dano = 15
        for oponente in oponentes:
            oponente.vida -= dano
        print(f"{self.nome} usa Chuva de Flechas e Causa {dano} de Dano a Todos os Inimigos!")

def importar_personagens(caminho):
    with open(caminho, 'r') as file:
        dados = json.load(file)

    personagens = []
    for dado in dados:
        if dado['classe'] == 'Guerreiro':
            personagens.append(Guerreiro(dado['nome'], dado['vida'], dado['ataque']))
        elif dado['classe'] == 'Mago':
            personagens.append(Mago(dado['nome'], dado['vida'], dado['ataque']))
        elif dado['classe'] == 'Arqueiro':
            personagens.append(Arqueiro(dado['nome'], dado['vida'], dado['ataque']))

    return personagens, len(personagens)

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda p: p.vida)

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[2]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])