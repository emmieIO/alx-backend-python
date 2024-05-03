#!/usr/bin/env python3
"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """8-make_multiplier.py"""
    def myfunc(multiplier: float) -> float:
        """inner function"""
        return multiplier * multiplier

    return myfunc
