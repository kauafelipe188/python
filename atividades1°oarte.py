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
# atividade15/3
# calculando a media de notas
# nota1 = int(input("digite a 1° nota: "))
# nota2 = int(input("digite a 2° nota: "))
# nota3 = int(input("digite a 3° nota: "))
# nota4 = int(input("digite a 4° nota: "))
# media = (nota1 + nota2 + nota3 + nota4) / 4
# print("a media das notas é:", media)
# atividade15/4
# verificando se um numero é par ou não
# numero = int(input("digite um numero: "))
# if numero % 2 == 0:
#     print("o numero é par")
# else:
#     print("o numero é impar")
# atividade15/5
# encontrar o maior numero da lista
# def encontrar_maior(lista):
#     maior = lista[0]
#     for numero in lista[1:]:
#         if numero > maior:
#             maior = numero
#     return maior
# numeros = [3, 5, 2, 9, 1, 4]
# print(f"O maior número é: {encontrar_maior(numeros)}")
# atividade15/11
# def ordenar_tarefas_por_prioridade(tarefas):
#     tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: tarefa[1], reverse=True)
#     return tarefas_ordenadas
# tarefas = [("Lavar o banheiro", 3), ("Estudar algoritmos", 5), ("jogar volei", 7)]
# tarefas_ordenadas = ordenar_tarefas_por_prioridade(tarefas)
# print("Tarefas ordenadas por prioridade:")
# for tarefa in tarefas_ordenadas:
#     print(tarefa)

# atividade16
# numero = int(input("digite um numero: "))
# if numero < 0:
#     print(numero * -1)
# else: 
#     print(numero)

# atividade17
# nome = str(input("insira seu nome: "))
# porção = 5.90
# qntd = int(input("insira uma quantidade de porções: "))
# if nome != "jerry" :
#     print(qntd * porção)

# # atividade18
# numero = int(input("digite um numero: "))
# if numero < 1000:
#     print("o numero é menor que 1000")
# if numero < 100:
#     print("o numero é menor que 100")    
# if numero < 10:
#     print("o numero é menor que 10") 
# if numero > 1000:
#     print("Obrigado!")

# atividade19
# nome = "kaua"
# cidade = "curitiba"
# estado = "parana"
# cep = 81234567
# nome2 = str(input("digite o nome: "))
# if nome2 == nome:
#     print(nome, cidade, estado, cep)
# if nome2 != nome:
#     print("esse usuario nao existe em nossa base de dados")

# atividade20
# numero1 = int(input("escreva um numero: "))
# numero2 = int(input("escreva outro numero numero: "))
# sinal = input("escolha a operação: ")
# op1 = "*"
# op2 = "-"
# op3 = "+"
# if sinal == op1:
#     print(numero1 * numero2)
# if sinal == op2:
#     print(numero1 - numero2)
# if sinal == op3:
#     print(numero1 + numero2)

# atividade21
# temp = float(input("coloque a temperatura: "))
# celcius = (temp - 32) / 1.8
# if celcius > 0:
#     print(f"{celcius:.2f}° celcius")
# if celcius < 0: 
#     print("Brr! Está frio aqui!")

# atividade22
# salariohr = float(input("digite o valor da hora: "))
# qntdhr = float(input("digite a qntd de hrs: "))
# dia = input("digite o dia da semana: ")
# salariotot = salariohr * qntdhr
# if dia == "domingo":
#     print(salariotot * 2)

# atividade23
# pntsnocartão = int(input("Digite a quantidade de pontos"))
# if pntsnocartão < 100:
#     taxabonus = 0.10
# if pntsnocartão > 100:
#     taxabonus = 0.15
# bonus = pntsnocartão * taxabonus
# print(f"o bonus é de: {bonus:.2f} pontos")   

# atividade24

# #atividade25
# media = float(input("digite a nota: "))
# if media < 7:
#     print("aprovado")
# else:
#     print("reprovado")

# #atividade26
# idade = int(input("digite a idade: "))
# if idade > 18:
#     print("de maior")
# else:
#     print("de menor")

# #atividade27
# valorgasto = int(input("Digite o valor gasto: "))
# if valorgasto < 50:
#     print("classe economica")
# if valorgasto > 50 and valorgasto < 100:
#     print("classe intemediaria")
# else:
#     print("classe executiva")

# atividade28
# idade = int(input("digite a idade: "))
# if idade >= 16:
#     print("pode votar")
# else:
#     print("não pode votar")

# #atividade29
# mesdoano = int(input("digite o numero do mes: "))
# if mesdoano == 1:
#     print("janeiro")
# if mesdoano == 2:
#     print("fevereiro")
# if mesdoano == 3:
#     print("março")
# if mesdoano == 4:
#     print("abril")
# if mesdoano == 5:
#     print("maio")
# if mesdoano == 6:
#     print("junho")
# if mesdoano == 7:
#     print("julho")
# if mesdoano == 8:
#     print("agosto")
# if mesdoano == 9:
#     print("setembro")
# if mesdoano == 10:
#     print("outubro")
# if mesdoano == 11:
#     print("novembro")
# if mesdoano == 12:
#     print("dezembro")
# else:
#     print("mes invalido")

# atividade30
# numero1 = int(input("escreva um numero: "))
# numero2 = int(input("escreva outro numero: "))
# if numero1 > numero2:
#     print("o primeiro numero é maior")
# elif numero1 < numero1:
#     print("o segundo numero é maior")
# else:
#     print("os numeros são iguais")

# atividade31
# idade1 = int(input("escreva a idade da primeira pessoa: "))
# nome1 = str(input("escreva o nome da primeira pessoa"))
# idade2 = int(input("escreva a idade da segunda pessoa: "))
# nome2 = str(input("escreva o nome da segunda pessoa"))
# if idade1 > idade2:
#     print("a pessoa mais velha é", nome1)
# elif idade1 < idade2:
#     print("a pessoa mais velha é", nome2)
# else:
#     print("as pessoas tem a mesma idade")

# atividade32
# nao teve

# atividade33
# idade1 = int(input("escreva a idade da pessoa: "))
# if idade1 <= 5 or idade1 > 105 :
#     print("a pessoa nao consegue digitar🤨")

# atividade34
# nome = str(input("escreva um nome: "))
# if nome == "huguinho" or "zezinho" or "luisiznho":
#     print("você é um dos 3 sobrinhos do pato donald")
# elif nome == "chiquinho" or "francisquinho":
#     print("você é um dos 2 sobrinhos do mickey mouse")
# else:
#     print("você não é ngm"}

# atividade35
# nota = float(input("Escreva sua nota: "))
# if nota  <= 0 :
#     print("impossivel")
# elif nota > 0 and nota <= 49:
#     print("reprovado")
# elif nota > 50 and nota <= 59:
#     print(1)
# elif nota > 60 and nota <= 69:
#     print(2)
# elif nota > 70 and nota <= 79:
#     print(3)
# elif nota > 80 and nota <= 89:
#     print(4)
# elif nota > 90 and nota <= 100:
#     print(5)
# elif nota > 90 and nota <= 100:
#     print("impossivel")
# else:
#     print("adicione uma nota certo animal")

# atividade36
# numero = int(input("digite um numero: "))
# if numero % 3 == 0:
#     print("fizz")
# elif numero % 5 == 0:
#     print("buzz")
# else:
#     print("fizzbuzz")

# atividade37
# ano = int(input("digite o ano: "))
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print("ano bissexto")
# else:
#     print("nao é ano bissexto")

# atividade38
# while True:
#     codigo = str(input("Olá "))
#     if codigo == "não":
#         break
#     print("voce quer continuar? ")
# print("okay, até a proxima")

# atividade39
# from math import sqrt
# while True:    
#     numero = int(input("escreva um numero inteiro: "))
#     if numero < 0:
#         print("impossivel")
#     elif numero > 0 :
#         print(sqrt(numero))
#     elif numero == 0 :
#         break

# atividade40
# numero = 5
# print("Contagem regressiva!")
# while True:
#     print(numero)
#     numero = numero - 1
#     if numero == 0:
#         break
# print("Agora!")

# atividade41
# senha = input("por favor, crie uma senha: ")
# while True:
#     confirmacao_senha = input("digite a senha novamente: ")
#     if confirmacao_senha == senha:
#         print("senha confirmada com sucesso!")
#         break
#     else:
#         print("senha errada. Tente novamente.")

# atividade42
# codigo = "4321"
# tentativas = 0
# while True:
#     pin = input("Digite o código PIN: ")
#     if pin == codigo:
#         print("Acesso liberado")
#         break
#     else:
#         tentativas += 1
#         print("Código incorreto. Tente novamente")

# print(f"Você tentou {tentativas} vezes.")

# atividade43
# ano = int(input("Digite o ano: "))
# def bissexto(ano):
#     if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#         return True
#     else:
#         return False
# pbissexto = ano + 1
# while not bissexto(pbissexto):
#     pbissexto += 1
# print(f"O próximo ano bissexto é {pbissexto}.")

# atividade44
# numero = 0
# while numero < 30:
#     print(numero)
#     numero += 2
# print("execução finaçizada")

# atividade45
# print("Você está pronto? ")
# numero = int(input("Por favor, digite um número: "))
# while True:
#     numero = numero - 1
#     if numero == 0:
#         break
#     print(numero)
# print("AGORA!")

# atividade46
# numero = int(input("Digite um número: "))
# if numero > 1:
#     for i in range(1, numero):
#         print(i)

# atividade47
# numero = int(input("Digite um numero como limite: "))
# numeroinicial = 1
# while numeroinicial <= numero:
#     print(numeroinicial)
#     numeroinicial *= 2

# atividade48
# numero = int(input("Digite um número como limite: "))
# base = int(input("Digite a base que será multiplicada: "))
# numeroinicial = 1
# while numeroinicial <= numero:
#     print(numeroinicial)
#     numeroinicial *= base

# atividade49
# nao tem

# atividade50
# soma = 0
# while soma <= 100:
#     numero = int(input("Digite um número: "))
#     soma += numero
# print("A soma é:", soma)

# atividade51
# import re
# def senhacerto(senha):
#     if len(senha) < 8:
#         return False
#     if not re.search("[A-Z]", senha):
#         return False
#     if not re.search("[a-z]", senha):
#         return False
#     if not re.search("[0-9]", senha):
#         return False
#     return True
# while True:
#     senha = input("Digite uma senha: ")
#     if senhacerto(senha):
#         print("Senha válida!")
#     else:
#         print("Senha inválida. A senha deve ter pelo menos 8 caracteres, conter pelo menos uma letra maiúscula, uma letra minúscula e um número.")

# atividade52
# import random
# numero = random.randint(1, 100)
# while True:
#     tentativa = int(input("adivinhe o número: "))
#     if tentativa < numero:
#         print("o número secreto é maior do que a tentativa.")
#     elif tentativa > numero:
#         print("o número secreto é menor do que a tentativa.")
#     else:
#         print("você adivinhou o número!")
#         break 

# atividade53
# saldo = 500
# def saque_valido(valor, saldo):
#     if valor % 10 != 0:
#         print("O valor de saque deve ser múltiplo de 10.")
#         return False
#     elif valor > saldo:
#         print(f"O valor de saque não esta disponivel")
#         return False
#     return True
# while True:
#     try:
#         valor_saque = int(input("Insira o valor de saque: R$ "))
#         if saque_valido(valor_saque, saldo):
#             print(f"Saque de R$ {valor_saque} realizado com sucesso!")
#             break
#     except ValueError:
#         print("Por favor, insira um valor numérico válido.")

# atividade54
# while True:
#     palavra1 = input("digite a primeira palavra: ")
#     palavra2 = input("digite a segunda palavra: ")
#     if len(palavra1) == len(palavra2):
#         print("as palavras tem a mesma quantidade de letras")
#         break
#     else:
#         print("as palavras sao diferentes, faça de novo")

# atividade55
# string = str(input("coloque uma palavra com o numero de caracteres escolhido: "))
# print("#"* len(string))

# atividade56
# string = input("digite uma string: ")
# while len(string) != 0:
#     traços = "-" * len(string)
#     print(string)
#     print(traços)
#     string = input("digite uma string: ")

# atividade57
# string = input("digite uma string: ")
# stringcom20 = string.rjust(20, "*")
# print(stringcom20)

# atividade58
# string = input("Digite uma palavra: ")
# tamanhoquadro = 30
# lenpalavra = len(string)
# espaço1 = (tamanhoquadro - 2 - lenpalavra) // 2
# espaço2 = tamanhoquadro - 2 - lenpalavra - espaço1
# print('*' * tamanhoquadro)
# print('*' + ' ' * espaço1 + string + ' ' * espaço2 + '*')
# print('*' * tamanhoquadro)

