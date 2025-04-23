#!/usr/bin/python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def func(num: float) -> float:
        return num * multiplier
    return func
