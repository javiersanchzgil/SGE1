def print_args(**args):
    print(args)


def main ():
    print_args(nombre="Javier", apellido = "Sanchez")
    print(saludo_doble("Javier", "Daniel"))


def saludo_individual(name):
    saludo = f"Hola, {name}"
    return saludo


def saludo_doble(name: str, name2: str) -> tuple[str,str]:
    """
    Saludo a dos personas,
        Args:
            name(str): Primera persona
            name2(str): Segunda persona


        :return:
         str: _description_
    """
    return saludo_individual(name),saludo_individual(name2)

if __name__ == "__main__":
    print("Comienzo programa")
    main()
    print("Fin del programa")