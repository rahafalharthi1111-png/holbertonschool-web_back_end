#!/usr/bin/env python3
"""
Return an asyncio.Task for wait_random with the given delay.
"""

import asyncio
import importlib

wait_random = importlib.import_module("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that wraps wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task object representing the coroutine execution.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
