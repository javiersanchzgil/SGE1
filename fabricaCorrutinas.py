import asyncio
import random


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
            print("BBBBBBBBBBBBBBBBBBBBBBBB")
            vRueda -= 1
            vChasis -= 1
            vMotor -= 1
            await salida_fabrica("coche")


async def concesionario(salida_fabrica):
    while True:
        obj = await  salida_fabrica.get()
        if obj == "coche":
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


async def main():
    entrada_fabrica = asyncio.Queue()
    salida_fabrica = asyncio.Queue()

    asyncio.create_task(ruedas(entrada_fabrica))
    asyncio.create_task(chasis(entrada_fabrica))
    asyncio.create_task(motor(entrada_fabrica))
    asyncio.create_task(fabrica(entrada_fabrica, salida_fabrica))
    asyncio.create_task(concesionario(salida_fabrica))

    await asyncio.sleep(50)


if __name__ == '__main__':
    print("Empezamos tarea")
    asyncio.run(main())
    print("Fin de la tarea")
