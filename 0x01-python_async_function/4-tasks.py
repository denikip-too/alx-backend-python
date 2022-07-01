#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async"""
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
