# Brute Force, O(n^2): Iterate all indices and maximise value

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        maxVal = val = 0
        for i in range(len(A)):
            for j in range(0,i):
                val = abs(A[i] - A[j]) + abs(i - j)
                maxVal = max(maxVal,val)
        return maxVal


# Mathematically Optimised O(n)
# Expression reduces to:
# Exp1: max(A[i]+i) - min(A[i]+i); Exp2: max(A[i]-i) - min(A[i]-i)
# max (Exp1, Exp2)

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        min1 = min2 = 2**31 - 1
        max1 = max2 = -2**31 + 1
        for i in range(len(A)):
            max1 = max(max1, A[i]+i)
            min1 = min(min1, A[i]+i)
            max2 = max(max2, A[i]-i)
            min2 = min(min2, A[i]-i)
        return max((max1-min1),(max2-min2))
