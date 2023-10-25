def burbuja (lista_numeros: list) -> list:
    lista = len(lista_numeros)
    lista_ordenada = lista_numeros.copy()

    for almacena in range(lista - 1):
        for verifica in range(lista - 1 - almacena):
            if lista_ordenada[verifica] > lista_ordenada[verifica + 1]:
                lista_ordenada[verifica], lista_ordenada[verifica + 1] = lista_ordenada[verifica + 1], lista_ordenada[verifica]

    return lista_ordenada

if __name__=="__main__":
    print(burbuja([8, 3, 1, 19, 14]))