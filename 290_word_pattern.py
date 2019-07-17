# easy
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ws = str.split()
        if len(pattern) != len(ws):
            return False
        m = dict()
        for i in range(len(ws)):
            if pattern[i] not in m.keys():
                if ws[i] in m.values():
                    return False
                else:
                    m[pattern[i]] = ws[i]
            else:
                if ws[i] != m[pattern[i]]:
                    return False
        return True
