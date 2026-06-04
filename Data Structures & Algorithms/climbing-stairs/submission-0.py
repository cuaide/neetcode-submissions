import math
class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        for k in range(n // 2 + 1):
            ones = n - 2 * k         
            total_steps = k + ones  
            result += math.factorial(total_steps) // (math.factorial(k) * math.factorial(ones))
        return result


                
