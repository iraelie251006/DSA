arr = [2, 1, 4, 3, 6, 5, 7, 9, 8, 10]
n = len(arr)
# Going to re implement two sum problem
def two_sum(arr, target):
    seen = {}
    for i in range(n):
        complement = target - arr[i]
