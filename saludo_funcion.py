
def saludo_cuadruple(name1, name2, name3, name4):
    return saludo_individual(name1), \
           saludo_individual(name2), \
           saludo_individual(name3), \
           saludo_individual(name4)

def saludo_multiple(principal,
                    *secuandarios, importante = "Familia", extra = "Amado Jefe"):
    return saludo_individual(principal), \
           saludo_individual(importante), \
           tuple(saludo_individual(n) for n in secuandarios) + \
           saludo_individual(extra)





def saludo_individual(name):
    saludo = f"Hola, {name}"
    return saludo

def main():
    for s in saludo_cuadruple("Cristina",
                              "Irene",
                              "Mayte",
                              "Manolo"):
        print(f"{s}")

    for s in saludo_multiple("Cristina",
                              "Irene",
                              "Mayte",
                              "Manolo,", extra = "Javier"):
        print(f"{s}")

if __name__ == "__main__":

    print("Comienzo de programa")
    main()
    print("Fin de programa")