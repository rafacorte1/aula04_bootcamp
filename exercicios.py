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
