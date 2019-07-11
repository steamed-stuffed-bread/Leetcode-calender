# medium
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        G = collections.defaultdict(set)
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
            
        v=set(G.keys())
                
        while len(G)>2:
            q = [x for x in G if len(G[x]) == 1]
            
            for leave in q:
                for y in G[leave]:
                    if leave in G[y]:
                        G[y].remove(leave)
                    del G[leave]
                    v.remove(leave)
        return list(v) if n!=1 else [0]
