#!/usr/bin/env python3
"module"

from typing import List
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes `n` coroutines of `wait_random` concurrently with a maximum
    delay of `max_delay`.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
