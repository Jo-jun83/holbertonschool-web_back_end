#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that collects
random numbers generated asynchronously into a list.
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collects 10 random numbers asynchronously from async_generator
    and returns them as a list.
    """
    random_numbers = []
    async for x in async_generator():
        random_numbers.append(x)
    return random_numbers
