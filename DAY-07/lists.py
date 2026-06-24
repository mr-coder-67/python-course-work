"""
DAY-07 — Lists and String Methods in Python

This file demonstrates core list operations and concepts including:
- Creating and initializing lists
- Basic operations (concatenation, repetition)
- Indexing and slicing with negative indices
- Membership testing (in, not in)
- Modifying lists (append, insert, extend, pop, remove, del, clear)
- Sorting and reversing
- Searching and counting (index, count)
- Aggregation functions (len, sum, min, max, any, all)
- List copying
- String methods (strip, testing methods like isalpha, isupper, etc.)
"""

# ============================================================================
# PART 1: CREATING AND INITIALIZING LISTS
# ============================================================================
print("=" * 60)  # Output: ============================================================
print("CREATING AND INITIALIZING LISTS")  # Output: CREATING AND INITIALIZING LISTS
print("=" * 60)  # Output: ============================================================

# Create an empty list using brackets
l = []
print("Empty list using []:", l)  # Output: Empty list using []: []

# Create an empty list using list() constructor
l = list()
print("Empty list using list():", l)  # Output: Empty list using list(): []
print("Type:", type(l))  # Output: Type: <class 'list'>

# Create a list with initial values
l = [10, 20, 30, 40, 50]
m = [4, 5, 6, 7, 8]
print("List l:", l)  # Output: List l: [10, 20, 30, 40, 50]
print("List m:", m)  # Output: List m: [4, 5, 6, 7, 8]


# ============================================================================
# PART 2: BASIC LIST OPERATIONS
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("BASIC OPERATIONS: CONCATENATION AND REPETITION")  # Output: BASIC OPERATIONS: CONCATENATION AND REPETITION
print("=" * 60)  # Output: ============================================================

# Concatenation: join two lists using +
concatenated = l + m
print("l + m (concatenation):", concatenated)  # Output: l + m (concatenation): [10, 20, 30, 40, 50, 4, 5, 6, 7, 8]

# Repetition: repeat a list using *
repeated = l * 2
print("l * 2 (repetition):", repeated)  # Output: l * 2 (repetition): [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]


# ============================================================================
# PART 3: INDEXING
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("INDEXING: ACCESSING INDIVIDUAL ELEMENTS")  # Output: INDEXING: ACCESSING INDIVIDUAL ELEMENTS
print("=" * 60)  # Output: ============================================================

print("List l:", l)  # Output: List l: [10, 20, 30, 40, 50]
print("l[0] (first element):", l[0])  # Output: l[0] (first element): 10
print("l[1] (second element):", l[1])  # Output: l[1] (second element): 20
print("l[3] (fourth element):", l[3])  # Output: l[3] (fourth element): 40
print("l[4] (fifth element):", l[4])  # Output: l[4] (fifth element): 50
print("l[-1] (last element):", l[-1])  # Output: l[-1] (last element): 50


# ============================================================================
# PART 4: SLICING
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("SLICING: EXTRACTING RANGES OF ELEMENTS")  # Output: SLICING: EXTRACTING RANGES OF ELEMENTS
print("=" * 60)  # Output: ============================================================

print("List l:", l)  # Output: List l: [10, 20, 30, 40, 50]
print("l[:3] (first three elements):", l[:3])  # Output: l[:3] (first three elements): [10, 20, 30]
print("l[2:5] (elements from index 2 to 4):", l[2:5])  # Output: l[2:5] (elements from index 2 to 4): [30, 40, 50]
print("l[:6] (all elements):", l[:6])  # Output: l[:6] (all elements): [10, 20, 30, 40, 50]
print("l[1:2] (element at index 1):", l[1:2])  # Output: l[1:2] (element at index 1): [20]
print("l[::-1] (reverse the entire list):", l[::-1])  # Output: l[::-1] (reverse the entire list): [50, 40, 30, 20, 10]
print("l[-1:-4:-1] (reverse last 3 elements):", l[-1:-4:-1])  # Output: l[-1:-4:-1] (reverse last 3 elements): [50, 40, 30]
print("l[-3::-1] (reverse from index -3 to start):", l[-3::-1])  # Output: l[-3::-1] (reverse from index -3 to start): [30, 20, 10]
print("l[-1:-4:-3] (every 3rd element from end):", l[-1:-4:-3])  # Output: l[-1:-4:-3] (every 3rd element from end): [50]


# ============================================================================
# PART 5: MEMBERSHIP TESTING
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("MEMBERSHIP TESTING: in and not in")  # Output: MEMBERSHIP TESTING: in and not in
print("=" * 60)  # Output: ============================================================

print("List l:", l)  # Output: List l: [10, 20, 30, 40, 50]
print("10 in l:", 10 in l)  # Output: 10 in l: True
print("10 not in l:", 10 not in l)  # Output: 10 not in l: False
print("50 in l:", 50 in l)  # Output: 50 in l: True
print("80 not in l:", 80 not in l)  # Output: 80 not in l: True


# ============================================================================
# PART 6: MODIFYING LISTS - ADDING ELEMENTS
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("MODIFYING LISTS: APPEND, INSERT, EXTEND")  # Output: MODIFYING LISTS: APPEND, INSERT, EXTEND
print("=" * 60)  # Output: ============================================================

l = [10, 20, 30, 40, 50]
print("Initial list:", l)  # Output: Initial list: [10, 20, 30, 40, 50]

# append: add a single element to the end
l.append(120)
print("After append(120):", l)  # Output: After append(120): [10, 20, 30, 40, 50, 120]

l.append(70)
print("After append(70):", l)  # Output: After append(70): [10, 20, 30, 40, 50, 120, 70]

# insert: add an element at a specific index
l.insert(1, 70)
print("After insert(1, 70):", l)  # Output: After insert(1, 70): [10, 70, 20, 30, 40, 50, 120, 70]

l.insert(5, 400)
print("After insert(5, 400):", l)  # Output: After insert(5, 400): [10, 70, 20, 30, 40, 400, 50, 120, 70]

# extend: add multiple elements (entire list) at the end
l.extend([120, 136, 345])
print("After extend([120, 136, 345]):", l)  # Output: After extend([120, 136, 345]): [10, 70, 20, 30, 40, 400, 50, 120, 70, 120, 136, 345]


# ============================================================================
# PART 7: MODIFYING LISTS - REMOVING ELEMENTS
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("MODIFYING LISTS: POP, REMOVE, DEL, CLEAR")  # Output: MODIFYING LISTS: POP, REMOVE, DEL, CLEAR
print("=" * 60)  # Output: ============================================================

print("Current list:", l)  # Output: Current list: [10, 70, 20, 30, 40, 400, 50, 120, 70, 120, 136, 345]

# pop: remove and return the last element
popped_element = l.pop()
print("After pop():", l, "- removed element:", popped_element)  # Output: After pop(): [10, 70, 20, 30, 40, 400, 50, 120, 70, 120, 136] - removed element: 345

# pop with index: remove element at specific index
popped_element = l.pop(3)
print("After pop(3):", l, "- removed element:", popped_element)  # Output: After pop(3): [10, 70, 20, 40, 400, 50, 120, 70, 120, 136] - removed element: 30

# remove: remove first occurrence of a value
l.remove(136)
print("After remove(136):", l)  # Output: After remove(136): [10, 70, 20, 40, 400, 50, 120, 70, 120]

l.remove(40)
print("After remove(40):", l)  # Output: After remove(40): [10, 70, 20, 400, 50, 120, 70, 120]

# del: delete element by index
del l[1]
print("After del l[1]:", l)  # Output: After del l[1]: [10, 20, 400, 50, 120, 70, 120]

del l[2]
print("After del l[2]:", l)  # Output: After del l[2]: [10, 20, 50, 120, 70, 120]

# clear: remove all elements from the list
l.clear()
print("After clear():", l)  # Output: After clear(): []


# ============================================================================
# PART 8: SORTING AND REVERSING
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("SORTING AND REVERSING")  # Output: SORTING AND REVERSING
print("=" * 60)  # Output: ============================================================

l = [200, 400, 50, 33, 45, 56, 78]
print("Original list:", l)  # Output: Original list: [200, 400, 50, 33, 45, 56, 78]

# sorted: returns a new sorted list (does not modify original)
sorted_l = sorted(l)
print("sorted(l):", sorted_l)  # Output: sorted(l): [33, 45, 50, 56, 78, 200, 400]
print("Original list after sorted():", l)  # Output: Original list after sorted(): [200, 400, 50, 33, 45, 56, 78]

# sort: modifies the list in-place
l.sort()
print("After l.sort():", l)  # Output: After l.sort(): [33, 45, 50, 56, 78, 200, 400]

# sorted with reverse=True
sorted_reverse = sorted(l, reverse=True)
print("sorted(l, reverse=True):", sorted_reverse)  # Output: sorted(l, reverse=True): [400, 200, 78, 56, 50, 45, 33]

# reverse: reverses the list in-place
l.reverse()
print("After l.reverse():", l)  # Output: After l.reverse(): [400, 200, 78, 56, 50, 45, 33]


# ============================================================================
# PART 9: SEARCHING AND COUNTING
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("SEARCHING AND COUNTING: INDEX AND COUNT")  # Output: SEARCHING AND COUNTING: INDEX AND COUNT
print("=" * 60)  # Output: ============================================================

print("List l:", l)  # Output: List l: [400, 200, 78, 56, 50, 45, 33]

# index: find the position of an element
index_pos = l.index(33)
print("l.index(33):", index_pos)  # Output: l.index(33): 6

# count: count occurrences of an element
count_val = l.count(78)
print("l.count(78):", count_val)  # Output: l.count(78): 1

# min and max: find smallest and largest elements
print("min(l):", min(l))  # Output: min(l): 33
print("max(l):", max(l))  # Output: max(l): 400


# ============================================================================
# PART 10: AGGREGATION FUNCTIONS
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("AGGREGATION: LEN, SUM, MIN, MAX, ANY, ALL")  # Output: AGGREGATION: LEN, SUM, MIN, MAX, ANY, ALL
print("=" * 60)  # Output: ============================================================

l = [10, 10, 20, 30, 40, 50]
print("List l:", l)  # Output: List l: [10, 10, 20, 30, 40, 50]

# len: count the number of elements
print("len(l):", len(l))  # Output: len(l): 6

# sum: add all elements
print("sum(l):", sum(l))  # Output: sum(l): 160

# min and max
print("min(l):", min(l))  # Output: min(l): 10
print("max(l):", max(l))  # Output: max(l): 50

# any: returns True if at least one element is truthy
print("any(l):", any(l))  # Output: any(l): True

# all: returns True if all elements are truthy
print("all(l):", all(l))  # Output: all(l): True

# Demonstrate any and all with different values
test_list_1 = [1, 2, 3, 4, 5, 0, 0, 0]
test_list_2 = [2, 3, 34, 5, 0, 0, 0]
print("any([1,2,3,4,5,0,0,0]):", any(test_list_1))  # Output: any([1,2,3,4,5,0,0,0]): True
print("all([2,3,34,5,0,0,0]):", all(test_list_2))  # Output: all([2,3,34,5,0,0,0]): False


# ============================================================================
# PART 11: LIST COPYING
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("LIST COPYING")  # Output: LIST COPYING
print("=" * 60)  # Output: ============================================================

l = [10, 10, 20, 30, 40, 50]
print("Original list l:", l)  # Output: Original list l: [10, 10, 20, 30, 40, 50]

# copy: create a shallow copy of the list
n = l.copy()
print("Copied list n:", n)  # Output: Copied list n: [10, 10, 20, 30, 40, 50]

# Modify the copied list
n.append(200)
print("After n.append(200):")  # Output: After n.append(200):
print("  Copied list n:", n)  # Output:   Copied list n: [10, 10, 20, 30, 40, 50, 200]
print("  Original list l:", l)  # Output:   Original list l: [10, 10, 20, 30, 40, 50]

# Additional demonstration of copying behavior
print("size of List:", len(l))  # Output: size of List: 6
print("sum of List:", sum(l))  # Output: sum of List: 160
print("maximum List:", max(l))  # Output: maximum List: 50
print("minimum List:", min(l))  # Output: minimum List: 10
print("any of true list:", any(l))  # Output: any of true list: True
print("all are true List:", all(l))  # Output: all are true List: True


# ============================================================================
# PART 12: STRING METHODS (BONUS)
# ============================================================================
print("\n" + "=" * 60)  # Output: (newline) ============================================================
print("STRING METHODS: STRIP AND TESTING")  # Output: STRING METHODS: STRIP AND TESTING
print("=" * 60)  # Output: ============================================================

# Strip methods: remove leading/trailing whitespace
s = "    Rishi     Varma    "
print("Original string:", repr(s))  # Output: Original string: '    Rishi     Varma    '
print("s.strip():", repr(s.strip()))  # Output: s.strip(): 'Rishi     Varma'
print("s.rstrip():", repr(s.rstrip()))  # Output: s.rstrip(): '    Rishi     Varma'
print("s.lstrip():", repr(s.lstrip()))  # Output: s.lstrip(): 'Rishi     Varma    '

# String testing methods: return boolean values
print("\nString testing methods:")  # Output: (newline) String testing methods:
print("s.startswith('  '):", s.startswith("  "))  # Output: s.startswith('  '): True
print("s.endswith('  '):", s.endswith("  "))  # Output: s.endswith('  '): True
print("s.isalpha():", s.isalpha())  # Output: s.isalpha(): False
print("s.isalnum():", s.isalnum())  # Output: s.isalnum(): False
print("s.istitle():", s.istitle())  # Output: s.istitle(): True
print("s.isupper():", s.isupper())  # Output: s.isupper(): False
print("s.islower():", s.islower())  # Output: s.islower(): False
print("s.isspace():", s.isspace())  # Output: s.isspace(): False
print("s.isidentifier():", s.isidentifier())  # Output: s.isidentifier(): False