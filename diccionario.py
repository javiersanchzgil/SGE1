from pprint import pprint
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

diccionario = {
    "dados" : {

    },
    "monedas" : {
        "cara" : {},
        "cruz" :{}
    }
}

moneda = ["cara","cruz"]
def tirar_moneda():
    return random.choice(moneda)

def tirar_dado():
    return random.randint(1,6)

if __name__ == "__main__":


    for x in range(11):
        diccionario["monedas"]["cara"][x] = 0
        diccionario["monedas"]["cruz"][x] = 0

    for x in range(3,19):
        diccionario["dados"][x] = 0

    for x in range (1000000):
        contdados = 0
        contcara = 0
        contcruz = 0
        for x in range(10):
            if tirar_moneda() == "cara":
                contcara = contcara + 1
            else:
                contcruz = contcruz + 1


        diccionario["monedas"]["cara"][contcara] +=1
        diccionario["monedas"]["cruz"][contcruz] += 1


        for x in range(3):
            contdados += tirar_dado()


        diccionario["dados"][contdados] +=1


    pprint(diccionario)
    nvecesmoneda = {5000,10000,20000,50000,100000,250000,500000,1000000}


    fig, ax = plt.subplots()
    # Colocamos una etiqueta en el eje Y
    ax.set_ylabel('Nº caras')
    # Colocamos una etiqueta en el eje X
    ax.set_title('Caras')
    # Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
    plt.bar(diccionario["monedas"]["cara"],nvecesmoneda)
    plt.savefig('barras_simple.png')
    # Finalmente mostramos la grafica con el metodo show()
    plt.show()

