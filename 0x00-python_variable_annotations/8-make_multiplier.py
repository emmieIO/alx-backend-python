#!/usr/bin/env python3
"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """8-make_multiplier.py"""
    def multiplier(num: float) -> float:
        """inner function"""
        return multiplier * num

    return inner
