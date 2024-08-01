# atividade1
# def tamanho_lista(lista):
#     return len(lista)
# print(tamanho_lista([1, 2, 3, 4, 5]))

# atividade2
# def range(numeros):
#     return max(numeros) - min(numeros)
# numeros = [1, 2, 3, 4, 5, 10]
# print(range(numeros))

# atividade4
# def lista_estrelas(numeros):
#     for numero in numeros:
#         print('*' * numero)
# numeros = [12, 5, 6, 2]
# lista_estrelas(numeros)

# atividade5
# def anagrama(string1, string2):
#     return sorted(string1) == sorted(string2)
# print(anagrama('abc', 'cab'))
# print(anagrama('abc', 'baa'))

# atividade6
# def soma_positivos(lista_de_numeros):
#     soma = 0
#     for numero in lista_de_numeros:
#         if numero > 0:
#             soma += numero
#     return soma
# print(soma_positivos([1, -2, 3, 4, -5]))
# print(soma_positivos([-1, -2, -3, -4, -5]))
# print(soma_positivos([10, 20, 30, -10, -20]))

# atividade7
# def numeros_pares(lista_de_numeros):
#     lista_de_pares = []
#     for numero in lista_de_numeros:
#         if numero % 2 == 0:
#             lista_de_pares.append(numero)
#     return lista_de_pares
# print(numeros_pares([1, 2, 3, 4, 5]))

# atividade8
# def lista_soma(primeira_lista, segunda_lista):
#     lista_somada = []
#     for indice in range(len(primeira_lista)):
#         soma_dos_itens = primeira_lista[indice] + segunda_lista[indice]
#         lista_somada.append(soma_dos_itens)
#     return lista_somada
# print(lista_soma([1, 2, 3, 4], [5, 6, 7, 8]))

# atividade9
# def sem_vogal(texto):
#     vogais = "aeiou"
#     texto_sem_vogal = ""
#     for caractere in texto:
#         if caractere not in vogais:
#             texto_sem_vogal += caractere
#     return texto_sem_vogal
# print(sem_vogal("xadrez"))

# atividade10
# def jogue_o_jogo(mesa, x, y, caractere):
#     mesa[x][y] = caractere
#     return mesa
# mesa = [[' ' for _ in range(3)] for _ in range(3)]
# jogue_o_jogo(mesa, 1, 1, 'X')
# for linha in mesa:
#     print(linha)
# jogue_o_jogo(mesa, 2, 2, 'X')
# for linha in mesa:
#     print(linha)
# jogue_o_jogo(mesa, 0, 0, 'X')
# for linha in mesa:
#     print(linha)

# atividade11
# def adicionar_contato(contatos, nome, numero):
#     contatos[nome] = numero
# def buscar_contato(contatos, nome):
#     return contatos.get(nome, "Contato não encontrado")
# def listar_contatos(contatos):
#     return "\n".join(f"{nome} {numero}" for nome, numero in contatos.items())
# def executar():
#     contatos = {}
#     while True:
#         comando 
))
#         if comando == 1:
#             nome = input("nome: ")
#             print(buscar_contato(contatos, nome))
#         elif comando == 2:
#             nome = input("nome: ")
#             numero = input("numero: ")
#             adicionar_contato(contatos, nome, numero)
#         elif comando == 3:
#             print(listar_contatos(contatos))
#         else:
#             print("comando invalido")
#             if comando == 0:
#                 break
# if __name__ == "__main__":
#     executar()

# atividade12
def adicionar_contato(contatos, nome, numero):
    if nome in contatos:
        if type(contatos[nome]) is list:
            contatos[nome].append(numero)
        else:
            contatos[nome] = [contatos[nome], numero]
    else:
        contatos[nome] = numero
def buscar_contato(contatos, nome):
    return contatos.get(nome, "Contato não encontrado")
def listar_contatos(contatos):
    lista = []
    for nome, numero in contatos.items():
        if type(numero) is list:
            for num in numero:
                lista.append(f"{nome} {num}")
        else:
            lista.append(f"{nome} {numero}")
    return "\n".join(lista)
def executar():
    contatos = {}
    while True:
        comando = int(input("comando (1 busca, 2 adiciona, 3 lista, 0 sai): "))
        if comando == 1:
            nome = input("nome: ")
            print(buscar_contato(contatos, nome))
        elif comando == 2:
            nome = input("nome: ")
            numero = input("numero: ")
            adicionar_contato(contatos, nome, numero)
        elif comando == 3:
            print(listar_contatos(contatos))
        elif comando == 0:
            break
        else:
            print("comando invalido")
if __name__ == "__main__":
    executar()

# atividade13
