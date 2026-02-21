#!/usr/bin/env python3
"""
Measure the average execution time of wait_n.
"""
import asyncio
import importlib
import time

wait_n = importlib.import_module("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function runs the asynchronous function wait_n with the given
    number of tasks (`n`) and maximum delay (`max_delay`), and calculates
    the total execution time. It returns the average time per task.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
