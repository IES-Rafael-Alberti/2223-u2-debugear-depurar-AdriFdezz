from src.algoritmo_burbuja import burbuja
def test_lista_ordenada():
        lista_entrada = [4, 2, 1, 3]
        lista_esperada = [1, 2, 3, 4]
        assert burbuja(lista_entrada) == lista_esperada