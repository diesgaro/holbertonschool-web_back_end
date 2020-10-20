#!/usr/bin/env python3
'''
    9. Let's duck type an iterable object
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        Function element_length
    '''
    return [(i, len(i)) for i in lst]
