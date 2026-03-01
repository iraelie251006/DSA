arr = [2, 1, 4, 3, 6, 5, 7, 9, 8, 10]

# Going to re implement two sum problem
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
