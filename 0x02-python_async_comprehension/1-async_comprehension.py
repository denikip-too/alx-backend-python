#!/usr/bin/env python3
"""Async Comprehensions"""
async_generator = __import__('0-async_generator').async_generator
import asyncio
import random


async def async_comprehension():
    """collect 10 random numbers using an async comprehensing over
    async_generator, then return the 10 random numbers"""
    return ([i async for i in async_generator()])
