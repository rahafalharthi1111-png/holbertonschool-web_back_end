#!/usr/bin/env python3
"""
Module for creating a tuple from a string and the square of an int or float.

Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Returns a tuple with the string and the square of the value as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the value as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple: A tuple containing the string and the squared value as a float.
    """
    return (k, float(v ** 2))
