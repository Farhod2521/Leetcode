class Solution:
    def minSteps(self, n: int) -> int:
        operations = 0 
        divisor =2
        while n >1:
            while n % divisor == 0:
                operations+=divisor
                n //= divisor
            divisor +=1

        return operations