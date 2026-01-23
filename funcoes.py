# %%
lista_numeros = [40, 50, 60, 70, 0, -408593, 1, 50]

def ordernar_lista(numeros):
    nova_lista = numeros.copy()
    for i in range(len(nova_lista)):
        for j in range(i+1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
    
    return nova_lista

nova_lista = ordernar_lista(lista_numeros)
print(nova_lista)

# %%
