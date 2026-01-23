# %%
import csv

path_file: str = 'exemplo.csv'

dados = []

with open(path_file, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    
    for linha in leitor_csv:
        dados.append(linha)
    
print(dados)
# %%
