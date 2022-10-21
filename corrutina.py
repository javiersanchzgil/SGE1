import asyncio
import random
import logging


def tirar_dado():
    return random.randint(1,6)

async def jugador (id):
    contdados = 0
    time = round(random.random()*5,3)
    await asyncio.sleep(time)
    for x in range(3):
        contdados += tirar_dado()

    print(f'runner({id} ha esperado {time} s. con tirada de dados de: {contdados}')
    return (id,time,contdados)

async def main ():
    tasks = [jugador(i) for i in range(10)]

    resultado = await asyncio.gather(*tasks)
    print(f'Resultados ordenados por id: {resultado}')

if __name__ == '__main__':
   print('Inicio programa')
   asyncio.run(main())
   print('FIN')
