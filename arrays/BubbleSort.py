# Bubble sort approach which is used to sort numbers in ascending order
# This algorithm will use time complexity of O(n^2) because of nested loop

# Note1 for range(n - 1) in the outer loop is for passes/times to loop through 
# so that we don't need to iterate through for the last time 
# because already the last element is in the right place.

# Note2 for range(n - i - 1) in the inner loop is for comparing adjacent pairs. 
# Where when we subtract by one we don't want when we use [j + 1] to go out of bounds 
# and we subtract i so that we will not happen to compare pairs that are already in the right place.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print("Sorted Array in ascending order: ", my_array)

# Bubble sort improvement imagine if our algorithm for the first iteration it sorted correctly 
# and there is nothing to swap but the algorithm will continue to check even if there is nothing to swap. 
# We have to "break" out the loop once our array is sorted.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array in ascending order: ", my_array)