class Pessoa:
    def __init__(self, *filhos, nome= None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo =Pessoa(nome = 'Renzo')
    luciano =Pessoa(renzo, nome= 'Luciano')
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramaraio'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)



#quando se trab com metodos o "p" é visto como primeiro parametro!#


