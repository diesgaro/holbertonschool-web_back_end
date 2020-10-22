#!/usr/bin/env python3
'''
2. Run time for four parallel comprehensions
'''

import asyncio
import time
from typing import List, Coroutine, Any

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    '''
    Coroutine that will execute async_comprehension four times in parallel
    and return the total runtime
    '''

    tasks: List[
        Coroutine[Any, None, None]
    ] = [
        async_comprehension() for n in range(4)
    ]

    start: float = time.time()

    await asyncio.gather(
        *tasks
    )

    end: float = time.time()
    totaltime: float = end - start
    return totaltime
