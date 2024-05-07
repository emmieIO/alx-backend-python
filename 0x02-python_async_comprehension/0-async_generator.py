#!/usr/bin/env python3
"""
0-async_generator.py
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
