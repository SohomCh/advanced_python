import asyncio

async def brew(name):
    print(f" {name} is brwing")
    await asyncio.sleep(3) ## non blocking
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew("masala chai"),
        brew("green tea"),
        brew("dudh chai"),




    )


asyncio.run(main())
    