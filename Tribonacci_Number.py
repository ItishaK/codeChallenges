# Leetcode: 1137. N-th Tribonacci Number
# This solution is through recursion and it leads to Time Exceeded error
# To deal with the Time Exceeded error use lru_cache function from functools module
# It improves the execution time through memoization technique

from functools import lru_cache
n = 38
@lru_cache
def tribo(n: int) -> int:    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)
        
output = tribo(n)
print(output) # Output is: 3831006429

# Solution through DP (Dynamic Programming)
# n = 38
# def tribo(n: int) -> int:
#     dp0, dp1, dp2 = 0, 1, 1
#     if n == 0:
#         return 0
#     for i in range(3, n+1):
#         dp0, dp1, dp2 = dp1, dp2, dp0 + dp1 + dp2    
#     return dp2
    
# output = tribo(n)
# print(output)
