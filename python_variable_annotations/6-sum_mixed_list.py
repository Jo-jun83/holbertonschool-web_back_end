#!/usr/bin/env python3
"""
This module contains a function that calculates the sum of a list
containing integers and floats, returning the result as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats and returns
    their sum as a float.
    """
    return sum(mxd_lst)
