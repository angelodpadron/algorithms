# fibonacci sequence

# brute force approach
# O(2^n) time complexity
# O(n) space complexity

def fib_bf(n):
    if n < 2:
        return 1

    return fib_bf(n-1) + fib_bf(n-2)

# memoization approeach
# O(2n) => O(n) time complexity
# O(n) space complexity

def fib_m(n, memo = None):
    if not memo:
        memo = [None] * (n + 1) 

    if n < 2:
        memo[n] = n

    if memo[n] is None:
        memo[n] = fib_m(n - 1, memo) + fib_m(n - 2, memo)

    return memo[n]

# grid traveler problem

# brute force approach
# O(2^(n + m)) time complexity
# O(n + m) space complexity

def grid_traveler_bf(n, m):
    if n == 1 and m == 1:
        return 1
    
    if n == 0 or m == 0:
        return 0

    return grid_traveler_bf(n - 1, m) + grid_traveler_bf(n, m - 1)

# print(grid_traveler_bf(13,13))

# memoization approach
# O(n * m) time complexity
# O(n * m) space complexity

def grid_traveler_m(n, m, memo = {}):
    key = str(n) + "," + str(m)
    
    # checks if the key or inverted key exists in the memo (i.e 2,1 or 1,2)
    if key in memo or key[::-1] in memo:
        return memo[key] if key in memo else memo[key[::-1]]

    if n == 1 and m == 1:
        return 1
    
    if n == 0 or m == 0:
        return 0

    if not (key in memo):
        memo[key] = grid_traveler_m(n - 1, m, memo) + grid_traveler_m(n, m - 1, memo)

    return memo[key]

print(grid_traveler_m(100,100))



    
