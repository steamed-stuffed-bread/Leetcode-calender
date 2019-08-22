class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.can = candidates
        self.helper(target, 0, [])
        return self.res

    def helper(self, target, left, out):
        if target < 0:
            return
        elif target == 0:
            self.res.append(out[:])
            return
        else:
            for i in range(left, len(self.can)):
                # every cycle uses non repeated value
                if i > left and self.can[i] == self.can[i-1]:
                    continue
                out.append(self.can[i])
                self.helper(target-self.can[i], i+1, out)
                out.pop()

