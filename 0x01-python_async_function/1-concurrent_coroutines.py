#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """This asynchronous coroutine spawns n wait_random
    coroutines concurrently
    with the specified max_delay and returns a
    list of delays in ascending order.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
