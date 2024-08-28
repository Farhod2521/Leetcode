class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        list_ = [0]
        for i in range(len(gain)):
            if i == 0:
                list_.append(gain[i])
            else:
                num  = list_[i] + gain[i]
                list_.append(num)
                
        return max(list_)