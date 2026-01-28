arr = [2, 1, 4, 3, 6, 5, 7, 9, 8, 10]

def two_sum (arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[complement] = i
    return None

print(two_sum(arr, 19))
