#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random


async def wait_n(n: int, max_delay: int) -> float:
    """return the list of all the delays (float values"""
    res = []
    temp = []
    for i in range(n):
        max_delay = random.uniform(0, max_delay)
        res.append(max_delay)
    while res:
        minimum = res[0]
        for x in res:
            if x < minimum:
                minimum = x
        temp.append(minimum)
        res.remove(minimum)
    return (temp)
