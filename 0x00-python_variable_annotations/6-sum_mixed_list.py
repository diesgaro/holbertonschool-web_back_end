#!/usr/bin/env python3
'''
    6. Complex types - mixed list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        Function that sum mixed list

        Arguments:
            mxd_lst (List): A List with float and integer values

        Return:
            float: the result of sum
    '''

    return sum(mxd_lst)
