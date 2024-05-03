#!/usr/bin/env python3
"""9-element_length.py"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """9-element_length.py"""
    return [(i, len(i)) for i in lst]
