import asyncio
from aiomultiprocess import Process
import asynclib
from multiprocessing import freeze_support

async def async_task():
    return "Async task result"

async def multiprocessing_task():
    loop = asyncio.get_event_loop()
    async with asynclib.Pool() as pool:
        result = await pool.spawn(async_task())
    return result

async def main():
    process = Process(target=multiprocessing_task)
    await process.start()
if __name__ == "__main__":
    freeze_support()
    asyncio.run(main())

# FIXIT: HERE