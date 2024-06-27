# atividade1
# nome = input("Digite seu nome:")
# apelido = input("Digite seu apelido:")
# endereço = input("digite seu endereço:")
# cidpos = input("Digite sua cidade e codigo postal:")
# #chamando inputs e printando
# print(nome,apelido,endereço,cidpos)

# atividade2
# nome1 = input("digite um nome:")
# ano = input("digite um ano:")
# print (nome1,"é um/a valente cavaleir@ nascid@ no ano de", ano , nome1, "acordou com um barulho terrivel: um dragão se aproximava da aldeia. Somente", nome1, "kauapoderia salvar os moradores da aldeia")

# atividade3
# cidade = "sao paulo"
# print(cidade)
# cidade = "rio de janeiro"
# print(cidade)

# atividade4
# string = input("digite uma string:")
# num = input("digite um numero inteiro:")
# float = input("digite um numero irracional:")
# print("string:",string)
# print("inteiro:",num)
# print("irracional:",float)

# atividade5
# fra1 = "se juntar"
# fra2 = "com a outra"
# print(fra1 + fra2)

# atividade6
# numero = int(input("coloque um numero:"))
# print(f"o resultado de {numero} vezes 5 é {5 * numero}")

# atividade7
# ano = int(input("coloque seu ano de nascimento aqui: "))
# nome = input("coloque seu nome: ")
# print(f"Olá {nome}, voce fará {2024 - ano} anos ao final de 2024")

# atividade8
# preço = float(input("coloque o preço: "))
# desconto = int(input("coloque a porcentagem do desconto: "))
# print(f"o preço com desconto é {preço - (preço * desconto / 100)} reais")
# print(f"o valor do desconto é {preço * desconto / 100} reais ")

# atividade9
# valor = int(input("coloque o valor da conta: "))
# PercentualGorjeta = int(input("coloque o percentual da gorjeta: "))
# print(f"o valor total é {valor + (valor * PercentualGorjeta / 100)} reais")

# atividade10
# valor = int(input("valor em real: "))
# dolar = int(valor / 5.51)
# print(f"o valor em dolar é {dolar} dolares")

# atividade11
# capital = int(input("digite o valor do capital: "))
# taxa = float(input("digite a taxa de juros "))
# tempo = int(input("digite o tempo em anos: "))
# print(f"O valor do juros é {capital * taxa * tempo} reais")

# atividade12
# numero1 = int(input("escreva o primeiro numero: "))
# numero2 = int(input("escreva o segundo numero: "))
# numero3 = int(input("escreva o terceiro numero: "))
# print(f"a media dos 3 numeros é :{(numero1 + numero2 + numero3) / 3}")

# atividade13
# altura = float(input("coloque a altura: "))
# largura = float(input("coloque a largura: "))
# print(f"o valor da area é {altura * largura} metros quadrados, e o perimetro é {2 *(largura + altura)}")

# atividade14
# celsius = float(input("temperatura em graus Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

# atividade15

# atividade16
# numero = int(input("digite um numero: "))
# if numero < 0:
#     print(numero * -1)
# else: 
#     print(numero)

# atividade17
nome = str(input("insira seu nome: "))
porção = 5.90
qntd = int(input("insira uma quantidade de porções: "))
if nome != "jerry" :
    print(qntd * porção)