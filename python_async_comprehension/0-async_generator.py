#!/usr/bin/env python3
"""
This module contains an asynchronous generator function that yields
random numbers.
"""

import asyncio
import random
from typing import List


async def async_generator()-> List[float]:
    """
    Asynchronous generator that yields 10 random numbers between 0 and 10,
    with a 1-second delay between each number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
