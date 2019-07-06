# easy
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                temp = stack[len(stack) - 1]
                if s[i] == '}' and temp != '{':
                    return False
                if s[i] == ']' and temp != '[':
                    return False
                if s[i] == ')' and temp != '(':
                    return False
                stack.pop()
        return len(stack) == 0
