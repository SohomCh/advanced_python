
import asyncio

async def brew_chai():
    print("brwing chai")
    await asyncio.sleep(4)
    print("readyyy")


asyncio.run(brew_chai())