# Contain duplicate algorithm

# This is O(n) linear time complexity and O(1) space
def containDuplicate(arr):
    # indices initialization
    left = 0
    right = len(arr) - 1

    # while loop to traverse an array
    while left < right:
        if arr[left] == arr[right]:
            return "Contain duplicates"
        elif arr[left] != arr[right]:
            right -= 1
            left += 1
    return "No duplicates"

arr = [1, 2, 4, 2, 4]
print(containDuplicate(arr))
