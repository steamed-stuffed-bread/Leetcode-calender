# medium
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        out = []
        candidates.sort()
        self.can = candidates
        self.helper(target, 0 ,out)
        return self.res

    def helper(self, target, left, out):
        if target < 0:
            return
        elif target == 0:
            self.res.append(out[:])
            return
        else:
            for i in range(left, len(self.can)):
                out.append(self.can[i])
                self.helper(target-self.can[i], i, out)
                out.pop()

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        out = []
        candidates.sort()
        self.can = candidates
        self.helper(target, 0 ,out)
        return self.res

    def helper(self, target, left, out):
        if target < 0:
            return
        elif target == 0:
            self.res.append(out[:])
            return
        else:
            for i in range(left, len(self.can)):
                if self.can[i] > target:
                    return
                self.helper(target-self.can[i], i, out + [self.can[i]])

