class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        prev=0
        curr=1
        for _ in range(n-1):
            prev , curr = curr, prev+curr
        return curr