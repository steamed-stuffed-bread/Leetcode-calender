# easy
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        G = dict()
        res = 0
        while i<n and j<n:
            if s[j] not in G.keys():
                G[s[j]] = j
                j = j+1
                res = max(res, j-i)
            else:
                del(G[s[i]])
                i = i+1
        return res
