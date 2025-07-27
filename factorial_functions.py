# 6-2 factorial_functions.py
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for num in [5, 7]:
    print(f"{num}! (재귀) = {factorial_recursive(num)}")
    print(f"{num}! (반복) = {factorial_iterative(num)}")