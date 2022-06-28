#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
import random
import time


async def measure_runtime():
    """measure the total runtime and return it"""
    for i in range(4):
        while True:
            timer_start = time.perf_counter()
            await asyncio.gather(async_comprehension())
            timer_stop = time.perf_counter()
            return (timer_stop - timer_start)
