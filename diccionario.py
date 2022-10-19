from pprint import pprint
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#creamos el diccionario con dados y monedas: cara y cruz
diccionario = {
    "dados" : {

    },
    "monedas" : {
        "cara" : {},
        "cruz" :{}
    }
}

#creamos un array con cara y cruz para la funcion tirar_moneda
moneda = ["cara","cruz"]

#función crear moneda
def tirar_moneda():
    return random.choice(moneda)

#creamos la misma función tirar_dado con valores del 1 al 6
def tirar_dado():
    return random.randint(1,6)


if __name__ == "__main__":

#Creamos un bucle que recorra 10 veces para inicializar monedas a 0 en las 10 tiradas, se le suma uno porque si no sale nunca cara
# por ejemlo hay que sumarle 0 veces también
    for x in range(11):
        diccionario["monedas"]["cara"][x] = 0
        diccionario["monedas"]["cruz"][x] = 0

#Igual con los dados del 3 al 19, porque hay que tirar 3 veces los dados, entonces mínimo saldrá un 3 y maximo un 18
    for x in range(3,19):
        diccionario["dados"][x] = 0


#Tiramos 1.000.000, 10 veces la moneda y sumamos al contador el número de veces que sale cara y otro con cruz para sumarle luego 1
#ala posición del número de veces
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


#Mismo bucle con dados pero con tiradas de 3 en vez de 10
        for x in range(3):
            contdados += tirar_dado()


        diccionario["dados"][contdados] +=1


#Imprimimos el diccionario
    pprint(diccionario)

    #Obtengo un diccionario más manejable solo con
    # los datos que me interesan(las veces que ha salido cara)
    dCaras = diccionario["monedas"]["cara"]
    pprint(dCaras)

    #En los diccionarios, no podemos suponer en las claves
    #están ordenadas, por lo que, para la lista de valores
    #del eje x, ordeno las claves
    dcx = sorted(dCaras.keys())
    print(dcx)

    #Creo la lista de valores x en el mismo orden que tiene las x
    #para que este ordenado
    dcy = []
    for x in dcx:
        dcy.append(dCaras[x])
    pprint(dcy)

    #Utilizo matplotlib para imprimir
    plt.figure()
    plt.plot(dcx,dcy)
    plt.xlabel("Nº caras")
    plt.ylabel("Nº veces")
    plt.show()



    # Hacemos la misma gráfica con las cruces
    dCruz = diccionario["monedas"]["cruz"]
    pprint(dCruz)

    dcx = sorted(dCruz.keys())
    print(dcx)

    dcy = []
    for x in dcx:
        dcy.append(dCruz[x])
    pprint(dcy)

    plt.figure()
    plt.plot(dcx, dcy)
    plt.xlabel("Nº cruces")
    plt.ylabel("Nº veces")
    plt.show()


    # Igual con los dados
    dDados = diccionario["dados"]
    pprint(dDados)

    dcx = sorted(dDados.keys())
    print(dcx)

    dcy = []
    for x in dcx:
        dcy.append(dDados[x])
    pprint(dcy)

    plt.figure()
    plt.plot(dcx, dcy)
    plt.xlabel("Nº dados")
    plt.ylabel("Nº veces")
    plt.show()




