#!/usr/bin/python3
"""MyInt is a rebel. MyInt has == and != operators inverted"""

class MyInt(int):
    """Class inherit from int, but invert == and !="""
    def __eq__(self, val):
    """Equality becomes inequality"""
        return super().__ne__(val)

    def __ne__(self, val):
    """Inequality becomes equality"""
        return super().__eq__(val)
