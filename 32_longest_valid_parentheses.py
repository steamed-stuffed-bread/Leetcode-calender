# hard
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 0:
                    left = i + 1
                else:
                    stack.pop()
                    res = max(res, i-left+1) if len(stack) == 0 else max(res, i-stack[len(stack)-1])
        return res
