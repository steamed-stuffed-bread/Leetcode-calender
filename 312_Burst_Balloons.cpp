class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int l = 1, i = 1, j = 0, k = 0;
        vector<vector<int>> dp(n+2, vector<int>(n+2, 0));
        
        for (l = 1; l <= n; ++l) {
            for (i = 1; i <= n-l+1; ++i) {
                j = i + l - 1;
                for (k = i; k <= j; ++k) {
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[k]*nums[i-1]*nums[j+1] + dp[k+1][j]);
                }
            }
        }
        
        return dp[1][n];
    }
};
