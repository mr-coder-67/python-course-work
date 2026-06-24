"""Dict examples cleaned from REPL transcript.

This file contains top-level examples demonstrating valid dictionary
operations. Erroneous operations are shown inside try/except blocks
so the script runs without crashing.
"""


# create empty dict in two ways
# 1) literal `{}` is the most common
# 2) `dict()` constructs an empty dict (useful for dynamic construction)
d = {}
print('d initially:', d)
d = dict()
print('d after dict():', d)

# using different key types: keys must be hashable (immutable)
# integers, floats and complex numbers are valid keys
d[1] = 'int'
d[1.23] = 'float'
d[1 + 30j] = 'complex'
print('d with varied keys:', d)

# trying to use unhashable keys (like list or set) raises TypeError
try:
    d[[1, 2, 3]] = 'list'
except TypeError as e:
    print('Cannot use list as key:', e)

try:
    d[{1, 2, 3}] = 'set'
except TypeError as e:
    print('Cannot use set as key:', e)

# tuple is hashable and can be used as a key
d[(1, 2, 3)] = 'tuple'
print('after adding tuple key:', d)

# boolean keys are hashable; note True == 1 so True and 1 collide
d[False] = 'bool'
print('after adding False key:', d)

# reset `d` to a fresh dict (avoids collisions with earlier examples)
d = {}
d[20] = 23.3
d[2] = 'sdfghj'
print('d partial:', d)

# accessing a missing key with `d[key]` raises KeyError
# use `d.get(key, default)` to avoid exceptions
try:
    print('d[3]:', d[3])
except KeyError:
    print('Key 3 not found (KeyError)')

# dictionaries can store values of any type
d[4] = 3 + 4j
d[5] = [1, 2, 3]
d[6] = (1, 2, 3)
d[7] = {1, 3}
d[8] = {1: 3}
d[9] = False
print('d full:', d)

# simple numeric dict example
d = {1: 2, 2: 2, 3: 2, 4: 2}
print('numeric dict:', d)

# dict does not support concatenation or repetition with + or *
try:
    _ = d + d
except TypeError as e:
    print('Cannot add dicts:', e)

try:
    _ = d * 4
except TypeError as e:
    print('Cannot multiply dict by int:', e)

# example: mapping student names to scores
d = {'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
print("manoj's score:", d['manoj'])
print("ashrutha's score:", d['ashrutha'])

# use `get()` to provide a default when a key may be missing
print("supriya with get():", d.get('supriya'))
print("akhil with get(default):", d.get('akhil', 'user not found'))

print("manoj in d:", 'manoj' in d)
print("'bhagravi' not in d:", 'bhagravi' not in d)

# view keys, values, and items (iterable views)
print('keys():', d.keys())
print('values():', d.values())
print('items():', d.items())

# get sorted keys and basic stats
print('sorted keys:', sorted(d))
print('min key (lexicographic):', min(d))
print('max key (lexicographic):', max(d))
print('len(d):', len(d))

# update an existing value
print("d['dinesh']:", d['dinesh'])
d['dinesh'] = 100
print('after update d:', d)

# add new key and bulk update using `update()`
d['rishi'] = 67
print('after adding rishi:', d)

d.update({'parneeth': 90, 'ajay': 80})
print('after update with dict:', d)

# remove and return the last inserted (as of Python 3.7+) item
print('popitem():', d.popitem())
print('after popitem d:', d)

print("pop('manoj'):", d.pop('manoj'))
print('after pop manoj d:', d)

# deleting keys with `del` (raises KeyError if key missing)
del d['parneeth']
print('after del parneeth:', d)

# safe deletion: check membership first
if 'rishi' in d:
    del d['rishi']
print('after conditional del rishi (if existed):', d)

# clear all items from the dictionary
d.clear()
print('after clear d:', d)

# setdefault: return existing value or set and return default
d = {'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
print("setdefault existing 'manoj':", d.setdefault('manoj', 0))
print("setdefault new 'chutkii':", d.setdefault('chutkii', 87))
print('final d:', d)