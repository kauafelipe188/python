# atividade1
# def media():
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
#     nota3 = float(input("Digite a terceira nota: "))
#     media = (nota1 + nota2 + nota3) / 3
# media()

# atividade2
# def printa_varias_vezes(texto, vezes):
#     for i in range(vezes):
#         print(texto)
# printa_varias_vezes("macaco", 5)

# atividade3
# def quadrado_hashtag(tamanho):
#     for i in range(tamanho):
#         print("#" * tamanho)
# quadrado_hashtag(5)

# atividade4
# def mesaxadrez(lado):
#     for i in range(lado):
#         linha = ""
#         for j in range(lado):
#             linha += str((i + j) % 2)
#         print(linha)
# mesaxadrez(50)

# atividade6
# def linha(inteiro, string):
#     if len(string) == 0:
#         string = "*"
#     else:
#         string = string[0]
#         print(string * inteiro)
# linha(10, "macaco")

# atividade7
# def caixa_hashtag(altura, largura=10):
#     if altura > 0:
#         for _ in range(altura):
#             print(largura * "#")
# caixa_hashtag(5, 10)

# atividade8

# atividade9

# atividade10
# def mesmo_caractere(string, inteiro1, inteiro2):
#     if inteiro1 < 0 or inteiro1 >= len(string) or inteiro2 < 0 or inteiro2 >= len(string):
#         return False
#     return string[inteiro1] == string[inteiro2]
# print(mesmo_caractere("macaco", 0, 2))