# List of numbers to search in
l = [2, 3, 5, 6, 10, 34, 12]

# Ask the user for the element to find
search = int(input("Enter the element: "))

# Loop through list indexes from 0 to len(l)-1
for i in range(len(l)):
    # Compare each element at index i with the search value
    if l[i] == search:
        print(f"{search} is found at index-{i}")
        # Stop the loop once the element is found
        break
else:
    # This else runs only if the loop completes without a break
    print(f'{search} is not found')