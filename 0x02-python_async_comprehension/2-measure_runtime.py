#!/usr/bin/env python3

"""
Import async_comprehension from the previous file and
 write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Import async_comprehension from the previous file and
    write a measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    tasks = []
    for _ in range(4):
        tasks.append(async_comprehension())
    await asyncio.gather(*tasks)
    total_time = time.perf_counter() - start_time
    return total_time
