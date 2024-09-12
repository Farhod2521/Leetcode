"""
Boyer-Moore Algoritmi:
 Boyer-Moore Voting Algorithm bo'lib, bu algoritm qo'shimcha xotira talab qilmasdan (O(1) space complexity) va O(n) vaqt bo'yicha murakkablikda ishlaydi. Bu algoritm asosiy g'oyasi — bitta "nomzod" elementni tanlash va uni to'liq array bo'ylab ko'p ovoz olib qoldirishdir 


"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nomzod  =  None
        count  = 0  
        for num in nums:
            if count == 0:
                nomzod =  num
            count += (1 if num== nomzod else -1)
        
        return nomzod
        