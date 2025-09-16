# This is fibonacci approach using loops.

prev1 = 0
prev2 = 1

print(prev1)
print(prev2)

for i in range(19):
    newFibonacci = prev1 + prev2
    print(newFibonacci)
    prev1 = prev2
    prev2 = newFibonacci


# This is fibonacci approach using recursion technique.
# Recursion is technique where function calls itself over and over.
# Note: global keyword we use global keyword when we want to modify global variable. 

print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibonacci = prev1 + prev2

        print(newFibonacci)

        prev1 = prev2
        prev2 = newFibonacci
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(0, 1)