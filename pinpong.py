import asyncio


async def pinger(ping, pong):
    mensaje="Ping"
    print("Mandando ping")
    await ping.put(mensaje)
    await pong.get()
    print("Pong recibido")

async def ponger(ping, pong):
    await ping.get()
    print("Ping recibido")
    mensaje="Pong"
    print("Mandando pong")
    await pong.put(mensaje)

async def main():
    ping = asyncio.Queue()
    pong = asyncio.Queue()

    t1=asyncio.create_task(pinger(ping, pong))
    t2=asyncio.create_task(ponger(ping, pong))

    await asyncio.sleep(0.1)

if __name__ ==  '__main__':
    asyncio.run(main())

