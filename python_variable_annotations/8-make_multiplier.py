#!/usr/bin/env python3
"""
This module provides a function `make_multiplier` that generates
a multiplier function for floating-point numbers.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the
    specified multiplier.
    """
    def func(num: float) -> float:
        """
        Multiplies the given number by the multiplier specified
        in the outer function.
        """
        return num * multiplier
    return func
