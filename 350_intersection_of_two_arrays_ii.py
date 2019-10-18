# easy
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        G = dict()
        for e in nums1:
            if e not in G.keys():
                G[e] = 1
            else:
                G[e] = G[e]+1
        res = []
        for e in nums2:
            if e in G.keys() and G[e] != 0:
                res.append(e)
                G[e] = G[e]-1
        return res
