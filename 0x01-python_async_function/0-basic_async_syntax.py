#!/usr/bin/env python3
"""0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This asynchronous coroutine waits for a random
    delay between 0 and max_delay seconds (inclusive)
    and returns the delay value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
