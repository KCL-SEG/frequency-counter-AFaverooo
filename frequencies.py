"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for value in items:
        value = str(value)
        if value in frequencies.keys():
            frequencies[value] += 1
        else:
            frequencies[value] = 1
    return frequencies


#frequencies(['a','a','b','b','b','c'])
#frequencies([])
#frequencies([100, 'Hello', '100', '100', 100])
