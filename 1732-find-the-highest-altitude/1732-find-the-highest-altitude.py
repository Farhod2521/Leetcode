class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        list_ = [0]
        max_ = 0 
        for i in range(len(gain)):

            num  = list_[i] + gain[i]
            if max_ < num: 
                max_ = num
                
            list_.append(num)
                
        return max_