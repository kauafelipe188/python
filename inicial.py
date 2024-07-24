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