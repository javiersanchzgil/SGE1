
def saludo_multiple(principal, *secundarios):
     return (saludo_individual(principal),) + \
          tuple(saludo_individual(n) for n in secundarios)

def saludo_individual(name):
    saludo = f"Hola, {name}"
    return saludo

def main():
    for s in saludo_multiple ("Cristina",
                              "Irene",
                              "Mayte",
                              "Maite"):
        print(f"{s}")

if __name__ == "__main__":
    print("Comienzo programa")
    main()
    print("Fin del programa")