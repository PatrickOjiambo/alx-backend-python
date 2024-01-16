#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
"""
import random
import asyncio


async def async_generator() -> None:
    """
    Write a coroutine called async_generator that takes no arguments.
    """
    for i in range(10):
        await asyncio.sleep(1)
        randomNumber: float = random.uniform(0,10)
        yield randomNumber
