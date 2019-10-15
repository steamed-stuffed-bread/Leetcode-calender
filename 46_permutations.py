# medium
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs_permute(0, nums)
        return self.res
    
    def dfs_permute(self, start: int, out: List[int]):
        if start >= len(out):
            self.res.append(out)
        for i in range(start, len(out)):
            temp = out[start]
            out[start] = out[i]
            out[i] = temp
            self.dfs_permute(start+1, out[:])
            temp = out[start]
            out[start] = out[i]
            out[i] = temp
