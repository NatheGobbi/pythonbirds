class Pessoa:
    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
#quando se trab com metodos o "p" é visto como primeiro parametro!#


