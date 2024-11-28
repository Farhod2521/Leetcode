class Solution(object):
    def searchInsert(self, nums, target):
        # For loop orqali tekshiramiz
        for index, value in enumerate(nums):
            if value >= target:  # Target qiymati yoki undan katta qiymatni topsak
                return index
        # Agar target massiv oxirida bo'lishi kerak bo'lsa
        return len(nums)