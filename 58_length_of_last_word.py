# easy
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(s)):
            if s[i] != " ":
                if i != 0 and s[i-1] == " ":
                    cnt = 1
                else:
                    cnt = cnt + 1
        return cnt
