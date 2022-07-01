#!/usr/bin/env python3
"""Async Generator"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for i in range(0, 10):
        i = random.uniform(0, 10)
        yield i
        await asyncio.sleep(1)
