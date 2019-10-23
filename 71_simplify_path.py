class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(path):
            while i < len(path) and path[i] == "/":
                i = i+1
            start = i
            if i == len(path):
                break
            while i < len(path) and path[i] != "/":
                i = i+1
            end = i
            temp = path[start:end]
            if temp == "..":
                if stack:
                    stack.pop()
            elif temp != ".":
                stack.append(temp)
        if len(stack) == 0:
            return "/"
        res = ""
        for i in range(len(stack)):
            res = res + "/" + stack[i]
        return res
