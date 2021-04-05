# convert integer list to string, join, add 1, re-convert to list

class Solution:
    # @param A : list of integers
    # @return a list of integers
    
    def plusOne(self, A):
        s = [str(i) for i in A]
        num = int("".join(s))
        num += 1
        s = str(num)
        B = []
        for i in s: 
            B.append(int(i))
        return B
