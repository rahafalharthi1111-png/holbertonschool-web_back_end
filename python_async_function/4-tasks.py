#!/usr/bin/env python3
"""
Run multiple task_wait_random calls concurrently and return sorted delays.
"""

from typing import List
import asyncio
import importlib

task_wait_random = importlib.import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n task_wait_random coroutines concurrently,
    return list of delays sorted.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay in seconds for each task.

    Returns:
        List[float]: Sorted list of delays from all tasks.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
