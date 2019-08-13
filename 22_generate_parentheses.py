# medium
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        self.res = []
        self.helper(n,n,"")
        return self.res
    def helper(self, left, right, out):
        if left > right:
            return
        if left == 0 and right == 0:
            self.res.append(out)
            return
        else:
            if left > 0:
                self.helper(left - 1, right, out + "(")
            if right > 0:
                self.helper(left, right-1, out + ")")
