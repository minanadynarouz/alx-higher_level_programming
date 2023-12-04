#!/usr/bin/python3
"""MyInt is a rebel. MyInt has == and != operators inverted"""


class MyInt(int):
    """Class inherit from int, but invert == and !="""


    def __eq__(self, other):
        """Equality becomes inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality"""
        return super().__eq__(other)
