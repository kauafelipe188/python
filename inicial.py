#print("Olá mundo")

#print("estamos praticando a progamação")
#print("primeiro estamos praticando o comando print")
#print("este comando printa 3 linhas de texto")

#print("Meu nome Kaua")
#print("Minha casa")
#print(17)

#meu primeiro python
#nome1 = input("Digite seu nome:")
#print("Olá, " + nome1,"!")

#String F
#resultado = 25
#resultado2 = 30
#print(f"O resultado é {resultado}, e a conta dos dois valores é  {resultado2 + resultado}")


#nome = "kaua felipe"
#idade = 17
#skill1 = "python"
#nivel1 = "iniciante"
#skill2 = "html"
#nivel2 = "junior"
#skill3 = "JavaScript"
#nivel3 = "iniciante"
#minimo = 3000
#maximo = "∞"
#print(f"Olá, eu sou {nome} e tenho {idade} anos. Minhas habilidades são {skill1} no nível {nivel1}, {skill2} no nível {nivel2} e {skill3} no nível {nivel3}. Procuro um emprego que pague entre #{minimo} e {maximo} reais por mês.")


#ano = int(input("coloque seu ano de nascimento aqui: "))
#print(f"ao final de 2024 voce ter {2024 - ano} anos")


# altura = float(input("qual a sua altura?"))
# peso = float(input("qual o seu peso?"))
# imc = peso / (altura / 100) ** 2
# print(f"seu imc é {imc:.2f}")


# numero = int(input("digite um numero: "))
# if numero == 1984:
#     print("Orwell")

# #and
# numero = int(input("numero: "))
# if numero >= 5 and numero <= 8:
#     print("numero entre 5 e 8")


# #or
# numero = int(input("numero: "))
# if numero < 5 or numero > 8:
#     print("numero não esta entre 5 e 8")

#while
# numero = int(input("digite um numero: . ou digite -1 para parar"))
# while numero == -1:
# break
# print(numero ** 2)
# print ("progama encerrado, obrigado")

# while True:
#     codigo = input("Por favor insira o pin: ")
#     if codigo == "1234":
#         break
#     print("errado, tente de novo")

# print("PIN correto, obrigado")
# tentativas = 0
# while True:
#     codigo = input("Por favor insira o pin: ")
#     tentativas += 1
#     if codigo == "1234":
#         sucesso = True
#         break
#     if tentativas == 3:
#         sucesso = False
#         break
#         print("PIN correto, obrigado")
#     else:
#         print("acabou as tentativas, obrigado")

# numero = int(input("coloque um numero: "))
# while numero < 10:
#     print(numero)
#     numero += 1

# print("execução finaçizada")

# import re

# print(re.search("[A-Z]", "Senha"))
# print(re.search("[a-z]", "Senha"))
# print(re.search("[0-9]", "Senha"))

# import random

# numero_secreto = random.randint(1,100)
# print(numero_secreto)

# palvra = "banana"
# print(palvra *3)

# string = str(input("entrada: "))
# print(string)
# print("-"* len(string))

# palavra1 = input("digite a primeira palavra: ")
# palavra2 = input("digite a segunda palavra: ")
# if len(palavra1) > len(palavra2):
#     print(palavra1)
# elif len(palavra1) < len(palavra2):
#     print(palavra2)

# string = input("por favor digite uma string: ")
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[-1])

# while True :
#     numero = int(input("por favor, digite um numero"))
#     if numero == -1:
#         break
#     while numero > 0:
#         print(numero)
#         numero -= 1

# def message():
#     print("essa é a minha função")
#     message()

# def sete_irmãos():
#     print("A")
#     print("B")
#     print("C")
#     print("D")
#     print("E")
#     print("F")
#     print("G")
# sete_irmãos()
# def cumprimentar(nome):
#     print("Olá, " + nome + "!")

# def cumprimentar_varias(nome, vezes):
#     while vezes > 0:
#         cumprimentar(nome)
#         vezes -= 1
# cumprimentar_varias("kaua", 5)

# def minha_soma(a,b):
#     return a + b
# resultado = minha_soma(6, 7)
# print(resultado)

# numeros = []
# numeros.append(10)
# numeros.append(5)
# numeros.append(3)
# print(numeros)

# numero_de_itens = int(input("Quantos itens você quer adicionar? "))
# lista = []
# contador = 0
# while contador < numero_de_itens:
#     valor = input(f"Digite o valor {contador + 1}: ")
#     lista.append(valor)
#     contador += 1
# contador_impressao = 0
# print("Valores adicionados à lista:")
# while contador_impressao < len(lista):
#     print(lista[contador_impressao])
#     contador_impressao += 1
# lista=[]

# def imprimir_lista():
#     print("Lista atual:",lista)
# def adicionar_item():
#     if len(lista)==0:
#         novo_item=1
#     else:
#         novo_item=lista[-1]+1
#     lista.append(novo_item)
#     imprimir_lista()
# def remover_item():
#     if len(lista)>0:
#         lista.pop()
#     imprimir_lista()
# def main():
#     while True:
#         imprimir_lista()
#         escolha=input("Digite 'Adicionar' para adicionar um item, 'Remover' para remover um item ou 'Sair' para encerrar o programa: ").strip().lower()
#         if escolha=='adicionar':
#             adicionar_item()
#         elif escolha=='remover':
#             remover_item()
#         elif escolha=='sair':
#             print("Programa encerrado.")
#             break
#         else:
#             print("Escolha inválida. Tente novamente.")
# main()

# recebe uma lista como argumento
# show_talentos = [45, 44, 36, 39, 40 ]
# def mediana (minha_lista: list):
#     ordenada = sorted(minha_lista)
#     centro_lista = len(ordenada) // 2
#     return ordenada[centro_lista]

# print("a mediana é" , mediana(show_talentos))  # imprime 39.0

# idades = [1, 56 ,34, 22, 5, 77, 5]
# print("a mediana é" , mediana(idades))

# retorna uma lista
# def entrada_numeros():
#     numeros = []
#     while True:
#         entrada_usuario = input ("POr favor, digite um numero inteiro, deixe em branco para sair")
#         if len(entrada_usuario) == 0:
#             break
#         numeros.append(int(entrada_usuario))
#         return numeros

# def tamanho_lista(lista):
#     return len(lista)
# print(tamanho_lista([1, 2, 3, 4, 5]))

