# medium
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        b = []
        while len(a)!=0:
            b.append(a.pop())
        return ' '.join(b)
