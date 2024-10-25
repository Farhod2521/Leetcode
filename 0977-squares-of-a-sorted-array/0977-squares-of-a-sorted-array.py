class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_ = []
        for num in nums:
            nums_.append(num*num)
        return sorted(nums_)