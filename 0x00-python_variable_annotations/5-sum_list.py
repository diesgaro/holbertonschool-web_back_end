#!/usr/bin/env python3
'''
    5. Complex types - list of floats
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
        Function that sum a float list

        Arguments:
            input_list (List): A List with float values

        Return:
            float: the result of sum
    '''

    return sum(input_list)
