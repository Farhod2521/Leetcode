class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary =  bin(n)[2:]
        nums = ""
        for i in range(len(binary)):
            if binary[i] == '0':
                nums += '1'
            elif  binary[i] == '1':
                nums += '0'
        decimal = int(nums, 2)
        return decimal
