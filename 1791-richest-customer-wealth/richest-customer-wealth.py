class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        n = len(accounts)
        max =0
        for i in range(n):
            list = accounts[i]
            s = sum(list)
            if(s>max):
                max = s
        return max


        