class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<=1:
            return 0
        prev,curr = 0,0
        for n in range(2,len(cost)+1):
            prev,curr = curr, min((prev+cost[n-2]),(curr+cost[n-1]))
        return curr