'''
EXERCICIO IMPRIMA OLA MUNDO NA TELA
'''

print("Olám,Mundo")
'''
Trabalhe com str,input,float
'''
nome = str("Otavinho")
idade = int(23)
numeros = float(2.0)
'''
FORMATANDO STRING
'''
string = "Ola meoo"
print("{}".format(string))

'''
TRABALHE COM INPUTS 
Pergunte ao usuario qual a idade e nome do usuario
'''
usuario = str(input("Informe o seu usuario : "))
idade = int(input("Informe a sua idade: "))

'''
TRABALHE COM if else e elif 
Peça a nota de uma pessoa se a nota for maior que 7 passou se nao reprovou
'''
nota = float(input("Informe a sua nota : "))
if nota >= 7:
    print("Passou")
elif nota < 7:
    print("Reprovado")
else:
    print("Sei la oq eu coloco aqui kkk")

'''
TRABALHE COM while laço de repetiçao e for 
'''
nome = str(input("Informe o seu nome: "))
for letra in nome:
    print(letra)

c = 5
while c < 100:
    c += 1
    print(c)

'''
EXERCICIOS USANDO CLASS 
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''
class Bola:
    def __init__(self, cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        nova_cor = str(input("Digite uma nova cor: "))
        self.cor = nova_cor
        return self.cor

    def mostrar_cor(self):
        return "A cor e : {}".format(self.cor)


'''

'''
