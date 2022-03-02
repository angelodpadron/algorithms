from typing import List

# Fibonacci with naive approach

def fib_naive(n: int) -> int:
    if n < 2:
        return n
    
    return fib_naive(n-1) + fib_naive(n-2)

# Fibonacci with tabulation (Bottom Up)

def fib_with_tabulation(n: int) -> int:

    output = [0] * (n + 1)

    # base case
    output[1] = 1

    # calculate the rest of the secuence and store the values of it
    for i in range(2, n + 1):
        output[i] = output[i - 1] + output[i - 2]
    
    return output[n]

print("tabulation: ", fib_with_tabulation(1000))