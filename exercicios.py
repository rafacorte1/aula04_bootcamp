# %%
# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
from typing import Dict, Any

livro1: Dict[str, Any] = {
    "Título": "Game of Thrones",
    "Autor": "George R.R. Martin",
    "Ano": 2005
}

lista_elementos: list = livro1.items()
for elemento in lista_elementos:
    print(elemento)
# %%

livro2: Dict[str, Any] = {
    "Título": "Game of Thrones 2",
    "Autor": "George R.R. Martin",
    "Ano": 2005
}


# %%

lista_de_livros = {
    "livro1": {"Título": "Game of Thrones",
    "Autor": "George R.R. Martin",
    "Ano": 2005},
    
    "livro2":  {"Título": "Game of Thrones 2",
    "Autor": "George R.R. Martin",
    "Ano": 2007}
}

print(lista_de_livros['livro1']['Título'])
# %%

# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    print(i ** 2)
# %%
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista_linguagens = ["Python", "Java", "C++", "JavaScript"]

lista_linguagens.remove("C++")
print(lista_linguagens)
lista_linguagens.append('Ruby')
print(lista_linguagens)
# %%
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")
# %%
# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))
# %%
