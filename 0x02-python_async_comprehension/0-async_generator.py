#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Write a coroutine called async_generator that takes no arguments.
    """
    for i in range(10):

        randomNumber: float = random.uniform(0, 10)
        yield randomNumber
        await asyncio.sleep(1)
