# ===================== exercicio 4 =====================

'''
EXERCICIO: Escreva uma funcao que recebe um objeto de colecoes
e retorna o valor do maior numero dentro dessa colecao
faca outra funcao que retorna o menor numero dessa colecao
'''

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

lista = ([1,-2,1.2,87.2,1289,-7,0])

print(menor(lista))
print(maior(lista))