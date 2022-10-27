
def saludo_multiple(principal, *secundarios):
     return (saludo_individual(principal),) + \
          tuple(saludo_individual(n) for n in secundarios)



# *numeros al colocar el * te hace una lista que coge el numeros de datos que quieras
def suma(*numeros):
    return sum(numeros)


def altitud(plantas,ciudad = 700):
    return plantas*3 + ciudad

def saludo_individual(name):
    saludo = f"Hola, {name}"
    return saludo


def main():
    for s in saludo_multiple ("Cristina",
                              "Irene",
                              "Mayte",
                              "Maite"):
        print(f"{s}")

        print(suma(1,2,3,4,4,5,4,2,3,4,2,2))

    print(altitud(3))
    print(altitud(4,ciudad=650))

if __name__ == "__main__":
    print("Comienzo programa")
    main()
    print("Fin del programa")