#!/usr/bin/env python3
'''
1. Let's execute multiple coroutines at the same time with async
'''


import asyncio
import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    '''
    Async routine that spawn wait_random n times with the specified max_delay
    '''
    lst: List[float] = []
    i: int = 0
    while i < n:
        bisect.insort(lst, await wait_random(max_delay))
        # lst.append(await wait_random(max_delay))
        i += 1

    return lst
