#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay
between 0 and a specified maximum value (default is 10 seconds) and then
returns
the delay. It uses the 'random' module to generate the delay and 'asyncio' for
asynchronous operations.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
