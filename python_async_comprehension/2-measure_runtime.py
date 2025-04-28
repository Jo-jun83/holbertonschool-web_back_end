#!/usr/bin/env python3
"""This module measures the runtime of executing async comprehensions
concurrently."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measures the total runtime of executing the async_comprehension function
    four times concurrently using asyncio.gather."""
    tasks = []
    start = time.time()
    for i in range(4):
        tasks.append(async_comprehension())
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
