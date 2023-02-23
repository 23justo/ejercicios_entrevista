from lib.decorators import *

import random


def _get_random_pivot(lista: list) -> int:
    return random.choice(lista)

@clean_data_decorator
def ordenar_lista(lista: list) -> list:
    """
    ordenar una lista de enteros utilizando un pivote random
    param: lista: lista de enteros
    return: lista de enteros ordenada
    """
    if len(lista) < 2:
        return lista

    random_pivot = _get_random_pivot(lista)
    lista_por_partes = {
        'menores': get_menores(lista, random_pivot),
        'iguales': get_iguales(lista, random_pivot),
        'mayores': get_mayores(lista, random_pivot)
    }

    return ordenar_lista(lista_por_partes['menores']) + lista_por_partes['iguales'] + ordenar_lista(lista_por_partes['mayores'])

def get_menores(lista, random_pivot):
    return [menor_iter for menor_iter in lista if menor_iter < random_pivot]

def get_iguales(lista, random_pivot):
    return [menor_iter for menor_iter in lista if menor_iter == random_pivot]

def get_mayores(lista, random_pivot):
    return [menor_iter for menor_iter in lista if menor_iter > random_pivot]

if __name__ == '__main__':
    randomlist = []
    for i in range(0,15):
        n = random.randint(1,30)
        randomlist.append(n)
    print(ordenar_lista(randomlist))
    