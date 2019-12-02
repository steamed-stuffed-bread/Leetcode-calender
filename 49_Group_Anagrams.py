class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = dict()
        for s in strs:
            tmp = list(s)
            sorted_s = ''.join(sorted(tmp))
            if sorted_s not in res:
                res[sorted_s] = []
            res[sorted_s].append(s)
        return res.values()
