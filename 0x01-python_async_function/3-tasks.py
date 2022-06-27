#!/usr/bin/env python3
"""returns asyncio.Task"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int):
    """returns asyncio.Task"""
    return (asyncio.Task(wait_random()))
