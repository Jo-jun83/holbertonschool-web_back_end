#!/usr/bin/env python3
"""
This module defines a function `element_length` that takes an iterable of
sequences
and returns a list of tuples, where each tuple contains a sequence and its
length.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of sequences as input and returns
    a list of tuples.
    Each tuple contains a sequence from the input and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
