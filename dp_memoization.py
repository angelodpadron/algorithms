# fibonacci sequence

# brute force approach
# O(2^n) time complexity
# O(n) space complexity

def fib_bf(n):
    if n < 2:
        return 1

    return fib_bf(n-1) + fib_bf(n-2)

# memoization approach
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

# print(grid_traveler_m(100,100))


# can sum problem 

# brute force approach
# O(n^m) time complexity, beign n = target and m = nums array length
# O(m) space complexity

def can_sum_bf(target, nums): 

    if target == 0:
        return True
    
    if target < 0:
        return False

    for num in nums:
        if (can_sum_bf(target - num, nums)):
            return True

    return False

# print(can_sum_bf(28, [7,14]))

# memoize approach
# O(m * n) time complexity, same variables as before
# O(m) space complexity

def can_sum_m(target, nums, memo = {}): 

    if target in memo:
        return memo[target]

    if target == 0:
        return True
    
    if target < 0:
        return False

    memo[target] = False

    for num in nums:
        if (can_sum_m(target - num, nums, memo)):
            memo[target] = True
            break

    return memo[target]

# print(can_sum_m(3000, [7,14]))


# how to sum problem

# brute force approach
# O(n^m) time complexity
# O(m) space complexity

def how_sum_bf(target, nums):

    if target == 0:
        return []
    
    if target < 0:
        return None

    for num in nums:
        res = how_sum_bf(target - num, nums)
        if not (res is None):
            res.append(num)
            return res     
            
    return None

# print(how_sum_bf(300, [7,14]))

# memoize approach
# O(m * n) time complexity, same variables as before
# O(m) space complexity

def how_sum_m(target, nums, memo = {}):

    if target == 0:
        return []
    
    if target < 0:
        return None

    if target in memo:
        return memo[target]
    
    memo[target] = None

    for num in nums:
        res = how_sum_m(target - num, nums, memo)
        if not (res is None):
            res.append(num)
            memo[target] = res
            break
    
    return memo[target]

# print(how_sum_m(600, [7,14]))


# best sum problem

# brute force approach
# O(n^m * m) time complexity
# O(m^2) space complexity, shortest could be m sized in the worst case

def best_sum_bf(target, nums):

    if target == 0:
        return []

    if target < 0:
        return None

    shortest = None
    
    for num in nums:
        remainder_combination = best_sum_bf(target - num, nums)

        if not (remainder_combination is None):
            remainder_combination.append(num)

            if shortest is None or len(remainder_combination) < len(shortest):
                shortest = remainder_combination

    return shortest

# print(best_sum_bf(8, [1,4,5]))

# memoization approach
# O(n * m^2) time complexity
# O(m^2) space complexity

def best_sum_m(target, nums, memo = {}):

    if target == 0:
        return []

    if target < 0:
        return None

    if target in memo:
        return memo[target]

    shortest = None    

    for num in nums:
        remainder_combination = best_sum_m(target - num, nums, memo)

        if not (remainder_combination is None):
            current_combination = remainder_combination.copy()  # here the reason of the m^2 from the time complexity
            current_combination.append(num)

            if shortest is None or len(current_combination) < len(shortest):
                shortest = current_combination

    memo[target] = shortest # and here the reason of the m^2 from the space complexity
    
    return shortest

# print(best_sum_m(675, [5,20,50,100,200]))


# can construct problem

# brute force approach
# blabla
# blabla

def can_construct_bf(target, wordBank):

    if not target:
        return True

    for word in wordBank:
        if word[0] == target[0] and word in target:
            suffix = target[len(word):]
            if can_construct_bf(suffix, wordBank):
                return True
    
    return False


print(can_construct_bf("abcdabf", ["ab","c","e","d"]))