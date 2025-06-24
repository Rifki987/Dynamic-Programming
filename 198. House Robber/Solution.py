class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxim_money=[0,0]
        for n,money in enumerate(nums):
            maxim_money[0],maxim_money[1] = maxim_money[1],max(maxim_money[0]+money,maxim_money[1])
        return maxim_money[1]