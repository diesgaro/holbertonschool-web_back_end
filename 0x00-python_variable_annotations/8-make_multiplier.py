#!/usr/bin/env python3
'''
    8. Complex types - functions
'''

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        Function that make a function to multiplies a float argument

        Arguments:
            multiplier (float): A float number

        Return:
            Callable: a function that multiplies
    '''
    def f(n: float):
        '''
            Function that multiplies two arguments

            Arguments:
                n (float): A float number

            Return:
                Float: the result of multiplies
        '''

        return n * multiplier
    
    return f    
