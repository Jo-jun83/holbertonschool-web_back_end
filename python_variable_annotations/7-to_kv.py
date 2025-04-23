#!/usr/bin/python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    square = v * v
    return (k, square)
