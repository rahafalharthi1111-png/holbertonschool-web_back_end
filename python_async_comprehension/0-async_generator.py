#!/usr/bin/env python3
"""
Asynchronously yields 10 random float numbers between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine waits 1 second between each yield and produces a
    random floating-point number in the range [0, 10) using the random module.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        float_number = random.uniform(0, 10)
        yield float_number
