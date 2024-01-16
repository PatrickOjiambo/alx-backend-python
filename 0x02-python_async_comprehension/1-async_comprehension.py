#!/usr/bin/env python3
"""
Import async_generator from the previous task and then
write a coroutine called async_comprehension that takes no arguments.
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> None:
    """
    Import async_generator from the previous task and then
    write a coroutine called async_comprehension that takes no arguments.
    """
    the_numbers = [i async for i in async_generator]
    print(the_numbers)
