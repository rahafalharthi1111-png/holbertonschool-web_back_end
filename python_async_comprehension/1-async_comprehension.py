#!/usr/bin/env python3
"""
Module for collecting random floats asynchronously using async comprehension.

"""
from typing import List
import importlib

async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats from async_generator using async comprehension.

    Returns:
        List[float]: List of 10 random floats.
    """
    return [i async for i in async_generator()]
