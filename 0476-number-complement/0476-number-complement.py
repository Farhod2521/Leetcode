class Solution:
    def findComplement(self, num: int) -> int:
        binary =  bin(num)[2:]
        nums = ""
        for i in range(len(binary)):
            if binary[i] == '0':
                nums += '1'
            elif  binary[i] == '1':
                nums += '0'
        decimal = int(nums, 2)
        return decimal
