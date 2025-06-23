class Solution(object):
   def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        prev=1
        curr=1
        for _ in range(n-1):
            nex = prev+curr
            prev = curr
            curr = nex
        return nex
