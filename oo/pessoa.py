class Pessoa:
    def __init__(self, nome='Charles Silva'): # o __init__ é um método
        self.nome = nome # o ATRIBUTO e o nome que esta conectado com o self no caso o sel.nome
        # os atributos de instancia e de objetos são criados atraves do metodo especial __init__

    def comprimentar(self): # o comprimentar é um método
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa('Noam') # podemos alterar o nome do objeto já na construção
    print(p.comprimentar())
    print(p.nome)
    p.nome = 'Silva'