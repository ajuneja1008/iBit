# Initiate sum as 0, maxSum as the first element
# Add all indexes into sum and replace maxSum is sum increases
# If sum becomes < than zero means that a large negatice number was added, reset the sum to 0

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sum , maxSum = 0 , A[0]
        for i in range (1,len(A)):
            sum += A[i]
            maxSum = max(sum,maxSum)
            if (sum < 0):
                sum = 0
            
        return maxSum

