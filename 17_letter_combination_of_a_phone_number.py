# medium
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.G = {'2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"}
        self.digits = digits
        self.res = []
        self.helper(0,"")
        return self.res
    
    def helper(self,h,out):
        if h == len(self.digits):
            self.res.append(out)
            return
        s = self.G[self.digits[h]]
        for i in range(len(s)):
            self.helper(h+1, out+s[i])
