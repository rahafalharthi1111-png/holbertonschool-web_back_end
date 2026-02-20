#!/usr/bin/env python3
"""
Basic annotations - element_length
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each element and its length
    """
    return [(i, len(i)) for i in lst]
