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
def mesaxadrez(lado):
    for i in range(lado):
        linha = ""
        for j in range(lado):
            linha += str((i + j) % 2)
        print(linha)
mesaxadrez(50)
