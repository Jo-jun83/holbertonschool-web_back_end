#!/usr/bin/env python3
"""
This module contains a function `to_kv` that converts a key and a value
into a tuple where the key is a string and the value is the square of
the input number (int or float).
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and a value into a tuple where the key is a string
    and the value is the square of the input number (int or float).
    """
    square = v ** 2
    return (k, square)
