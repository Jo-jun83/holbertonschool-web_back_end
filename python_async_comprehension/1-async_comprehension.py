#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that collects
random numbers generated asynchronously into a list.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously from async_generator
    and returns them as a list.
    """
    return [i async for i in async_generator()][:10]
