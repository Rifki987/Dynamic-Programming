class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        n_0,n_1,n_2 = 0,1,1
        for _ in range(3,n+1):
            n_0,n_1,n_2 = n_1,n_2,n_0+n_1+n_2
        return n_2