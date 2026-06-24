
# Tuple
# 1) It is a container to store elements (can be heterogeneous)
# 2) It is immutable
# 3) Representation of a tuple uses parentheses: ()


# -- Tuple examples --
t = (1, 2, 3, 4, 5, 6)
k = (1, 2, 3, 4, 5, 6, 5)
print("tuple t:", t)
print("tuple k:", k)

# Concatenation and repetition
print("t + k:", t + k)
print("t * 3:", t * 3)

# Indexing and slicing
print("t[3]:", t[3])         # 0-based index -> fourth element
print("t[:4]:", t[:4])       # slice up to index 4 (exclusive)
print("t[::-1]:", t[::-1])   # reversed tuple

# Membership test
print("30 in t:", 30 in t)

# Useful built-ins
print("len(t):", len(t))
print("sum(t):", sum(t))
print("min(t):", min(t))
print("max(t):", max(t))
print("sorted(t):", sorted(t))

# Count and index methods
print("k.count(5):", k.count(5))
print("k.index(4):", k.index(4))

# Tuples can contain mutable objects (like lists)
h = (1, 2, 3, 4, [1, 2, 3221], 221, 233)
print("h before modifying inner list:", h)
h[4].append(10)  # modifying inner list is allowed
print("h after modifying inner list:", h)


# -- Set examples --
# 1) It is a container for unique, unordered elements
# 2) It is mutable

s = {1, 2, 3, 44, 2, 2}  # duplicates will be removed
print("set s (duplicates removed):", s)

# Add and update
s.add(211.122)
print("after add(211.122):", s)

print("1 in s:", 1 in s)

h = {12, 3, 312, 33, 4, 344, 3444, 3}
print("s | h (union):", s | h)
print("s.intersection(h):", s.intersection(h))
print("s - h (difference):", s - h)
print("s ^ h (symmetric difference):", s ^ h)

# Subset / Superset checks
print("s <= h:", s <= h)
print("s >= {1,2}:", s >= {1, 2})

# Modifying sets
s.add(200)
print("after s.add(200):", s)
s.update({201, 445, 65})
print("after s.update(...):", s)

popped = s.pop()
print("after pop(), popped element:", popped)
print("s now:", s)

# Remove vs discard
if 2 in s:
	s.remove(2)
s.discard(9999)  # no error if not present
print("after removals:", s)

c = h.copy()
c.add(20000)
print("copied set c (modified):", c)
print("original h remains:", h)

print("len(s):", len(s))
# sum may fail if non-numeric values exist; here all are numeric
print("sum(s):", sum(x for x in s if isinstance(x, (int, float))))
print("min(s):", min(s))
print("max(s):", max(s))
print("sorted(s):", sorted(s))