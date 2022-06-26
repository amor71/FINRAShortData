import asyncio
import time


def timeit(func):
    async def process(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **params)
        else:
            return func(*args, **params)

    async def helper(*args, **params):
        start = time.time()
        result = await process(func, *args, **params)
        print(
            f"{func.__name__}() >>> took {round(time.time() - start, 3)} seconds"
        )
        return result

    return helper
