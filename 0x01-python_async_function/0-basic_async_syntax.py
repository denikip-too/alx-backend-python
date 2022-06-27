#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10):
    """The basics of async"""
    max_delay = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return (max_delay)
