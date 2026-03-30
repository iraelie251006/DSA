# Contain duplicate file will contain
# the check for duplicate values
# this problem will include arrays
# probably use of two pointers 
# under fast and slow pointers
# using python
# implement in java later on

def containDuplicate(arr):
    # indices initialization
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == arr[right]:
            return "Contain duplicates"
        elif arr[left] != arr[right]:
            right -= 1
            left += 1
    return "No duplicates"

arr = [1, 2, 4, 2, 4]
print(containDuplicate(arr))
