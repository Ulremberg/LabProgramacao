class Pessoa:

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

def aniversario(self):
    ani = self.idade + 1
    return ani

def main():
    idade1 = int(input('Digite idade:\n'))
    nome1 = input('Digite seu nome:\n')
    pessoa1 = Pessoa(nome1, idade1)
    print(pessoa1.aniversario())

if __name__ == "__main__":
    main()