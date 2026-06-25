# patterns.py
# Print a star pattern using nested loops and a single input request.
# This code does not create any new functions.

n = int(input('Enter pattern size: '))
m = n // 2

for i in range(n):
    for j in range(n):
        # Print a star at the border, the diagonals, and the center lines.
        if (
            i == 0
            or i == n - 1
            or j == 0
            or j == n - 1
            or i == j
            or i + j == n - 1
            or i == m
            or j == m
        ):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
