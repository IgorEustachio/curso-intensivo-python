"""def fazer_sandwich(**ingredientes):
    print("Olá, você quer um sandwich com os seguintes ingredientes: ")
    for chave,ingrediente in ingredientes.items():
        print(ingrediente)

fazer_sandwich(a="presunto", b="queijo", c="alface")"""

def make_car(modelo, ano, *cor):
    print("o carro do modelo ",modelo,f", lançado no ano de {ano}", "tem as seguintes cores:")

    for cores in cor:
        print(cores)

make_car('subaru', 1987, "rosa", 'azul', 'preto')

