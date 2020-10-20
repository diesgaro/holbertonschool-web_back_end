#!/usr/bin/env python3
'''
    7. Complex types - string and int/float to tuple
'''

from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
        Function that takes str and int or float arguments and return a
        tuple with the str and te square of int/float

        Arguments:
            k (str): A string argument
            v (int/float): a Integer or Float argument

        Return:
            Tuple: a tuple with the result
    '''

    return (k, math.pow(v, 2))
