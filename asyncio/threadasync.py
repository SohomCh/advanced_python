import asyncio
import time
from concurrent.futures import ThreadPoolExcetor


def check_stock(item):
    print(f"checking {item}in store")
    time.sleep(3)
    return f"{item} stock:42"

async def main():
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result=await loop.run_forever(pool,check_store,"MasalaChai")
        print(result)


asyncio.run(main())

