

def demo_sets():
  # Create and display sets
  print("Create sets")
  s = {1, 2, 3, 4}
  print("s:", s)
  # cmnts: example -> s: {1, 2, 3, 4}  (set order may vary)

  s = set()
  print("empty s:", s)
  # cmnts: example -> empty s: set()

  # duplicate literals collapse into a single element
  s = {1, 1, 1, 1}
  print("deduplicated s:", s)
  # cmnts: example -> deduplicated s: {1}

  s = {345, 456, 456, 67, 2, 3, 4, 5}
  print("s:", s)
  # cmnts: example -> s: {2, 3, 4, 5, 67, 456, 345}  (order may vary)

  # add examples: .add() inserts a single hashable element
  s = set()
  s.add(1)
  s.add(3)
  s.add(45.56)
  s.add('dfgh')
  print("s after adds:", s)
  # cmnts: example -> s after adds: {1, 3, 'dfgh', 45.56}  (order may vary)

  # attempting to add unhashable types raises TypeError
  # adding unhashable types (like list, set, dict) raises TypeError
  try:
    s.add([1, 2, 3, 4])
  except TypeError as e:
    print("Cannot add list to set:", e)
    # cmnts: example -> Cannot add list to set: unhashable type: 'list'

  try:
    s.add(set())
  except TypeError as e:
    print("Cannot add set to set:", e)
    # cmnts: example -> Cannot add set to set: unhashable type: 'set'

  try:
    s.add({1: 2})
  except TypeError as e:
    print("Cannot add dict to set:", e)
    # cmnts: example -> Cannot add dict to set: unhashable type: 'dict'

  # set operations
  a = {1, 2, 3, 4, 5, 6, 7, 8, 10}
  b = {6, 7, 8, 9}
  # common set operations: union, intersection, symmetric difference, difference
  print("a | b:", a | b)
  # cmnts: example -> a | b: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
  print("a.union(b):", a.union(b))
  print("a & b:", a & b)
  # cmnts: example -> a & b: {6, 7, 8}
  print("a ^ b:", a ^ b)
  print("a - b:", a - b)
  print("b - a:", b - a)
  print("a.isdisjoint(b):", a.isdisjoint(b))
  print("a.isdisjoint({90,80}):", a.isdisjoint({90, 80}))

  # update, pop, remove, discard, clear
  # add/update multiple items
  a.add(17)
  a.add(18)
  a.update({12, 30, 15})
  print("a after updates:", a)
  # cmnts: example -> a after updates: {1,2,3,4,5,7,8,10,12,15,17,18,30} (order varies)

  # pop removes and returns an arbitrary element
  popped = a.pop()
  print("popped:", popped)
  # cmnts: example -> popped: 1  (actual value may differ)

  # safe removals
  # remove vs discard: discard won't raise if element absent
  a.discard(5)
  if 6 in a:
    a.remove(6)
  a.discard(10)
  print("a after removals:", a)
  # cmnts: example -> a after removals: {3,4,7,12,15,17,18,30}

  a.clear()
  print("a after clear:", a)
  # cmnts: example -> a after clear: set()

  # intersection update and copy
  a = {1, 2, 23, 57, 235}
  b = {1, 2, 4, 34}
  # intersection_update keeps only elements present in both
  a.intersection_update(b)
  print("a after intersection_update:", a)
  # cmnts: example -> a after intersection_update: {1, 2}

  # copying sets produces independent duplicates
  c = b.copy()
  c.add(12)
  d = c.copy()
  d.add(10)
  print("c:", c)
  # cmnts: example -> c: {1,2,4,34,12}
  print("d:", d)
  # cmnts: example -> d: {1,2,4,34,12,10}

  print("len(c):", len(c))
  print("min(c):", min(c))
  print("max(c):", max(c))
  print("sorted(c):", sorted(c))
  # cmnts: example -> sorted(c): [1, 2, 4, 12, 34]
  # sum only numeric values
  print("sum(c):", sum(x for x in c if isinstance(x, (int, float))))
  # cmnts: example -> sum(c): 53


def main():
  demo_sets()


if __name__ == "__main__":
  main()