import asyncio
import random


#Creamos las corrutinas ruedas, chasis y motor que esperan entre 0 y 1 segundo y manda por entrada_fabrica a
#la corrutina fabrica (bucle infinito).
async def ruedas(entrada_fabrica):
    while True:
        await asyncio.sleep(random.randint(0, 1))
        print("ruedas fabricadas")
        await entrada_fabrica.put("ruedas")


async def chasis(entrada_fabrica):
    while True:
        await asyncio.sleep(random.randint(0, 1))
        print("chasis fabricado")
        await entrada_fabrica.put("chasis")


async def motor(entrada_fabrica):
    while True:
        await asyncio.sleep(random.randint(0, 1))
        print("motor fabricado")
        await entrada_fabrica.put("motor")

#En la corrutina fabrica recoge las anteriores en los contadores y cuando tenga uno de cada espera entre 0 y 1 segundo,
# realiza un coche y lo manda a concesionario por salida_fabrica
async def fabrica(entrada_fabrica, salida_fabrica):
    vRueda = 0
    vChasis = 0
    vMotor = 0

    while True:
        obj_coche = await entrada_fabrica.get()

        if obj_coche == "ruedas":
            vRueda += 1
        elif obj_coche == "chasis":
            vChasis += 1
        elif obj_coche == "motor":
            vMotor += 1

        if vRueda > 0 and vChasis > 0 and vMotor > 0:
            await asyncio.sleep(random.randint(0, 1))
            print("COCHE FABRICADO")
            vRueda -= 1
            vChasis -= 1
            vMotor -= 1
            await salida_fabrica.put("coche")


#En la corrutina concesionario tan solo nos muestra que el coche esta ya en el concesionario
async def concesionario(salida_fabrica):
    while True:
        obj = await  salida_fabrica.get()
        if obj == "coche":
            print("COCHE EN CONCESIONARIO")


#En la corrutina main creamos las corrutinas
async def main():
    entrada_fabrica = asyncio.Queue()
    salida_fabrica = asyncio.Queue()

    asyncio.create_task(ruedas(entrada_fabrica))
    asyncio.create_task(chasis(entrada_fabrica))
    asyncio.create_task(motor(entrada_fabrica))
    asyncio.create_task(fabrica(entrada_fabrica, salida_fabrica))
    asyncio.create_task(concesionario(salida_fabrica))

    await asyncio.sleep(50)

#Corremos el programa
if __name__ == '__main__':
    print("Empezamos tarea")
    asyncio.run(main())
    print("Fin de la tarea")
