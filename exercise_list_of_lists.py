# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    if len(lista_de_listas) < 3:
        lista_de_listas[0][3:] = []
        del (lista_de_listas[1][0])
        del (lista_de_listas[1][0])
        lista_de_listas[1][2:] = []
        return lista_de_listas
    elif lista_de_listas[1] == []:
        lista_de_listas[0][2:] = []

        lista_de_listas[2][0:len(lista_de_listas[2]) - 2] = []
        return lista_de_listas
    else:
        lista_de_listas[0][2:] = []

        del (lista_de_listas[1][0])

        lista_de_listas[1][3:] = []
        lista_de_listas[2][0:len(lista_de_listas[2]) - 2] = []
        return lista_de_listas
