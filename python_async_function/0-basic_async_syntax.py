#!/usr/bin/env python3
"""
Module for asynchronous waiting with a random delay.

Functions:
    wait_random(max_delay: int = 10) -> float:
        Waits asynchronously for a random delay and returns it.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits asynchronously for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay used (in seconds).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
