# easy
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if (i >= len(strs[j])) or (strs[j][i] != strs[0][i]):
                    return strs[j][:i]
        return strs[0]
# easy
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        lens = [len(e) for e in strs]
        min_l = min(lens)
        res = ""
        same = True
        for i in range(min_l):
            c = strs[0][i]
            for e in strs:
                if c != e[i]:
                    same = False
                    break
            if same == False:
                break
            res = res+c
        return res
