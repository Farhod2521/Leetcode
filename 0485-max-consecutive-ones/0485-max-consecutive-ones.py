class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count_current = 0
        for num in nums:
            if num == 1:
                count_current += 1
            else:
                max_count = max(count_current, max_count)
                count_current =0
        max_count  =  max(max_count, count_current)
        return max_count
