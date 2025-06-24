class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        graph = [[0]*n for _ in range(m)]
        graph[0][0]=1
        for r_idx,row in enumerate(graph):
            for c_idx,value in enumerate(row):
                if r_idx>=1:
                    row[c_idx]+=graph[r_idx-1][c_idx]
                if c_idx>=1:
                    row[c_idx]+=graph[r_idx][c_idx-1]
        return graph[m-1][n-1]