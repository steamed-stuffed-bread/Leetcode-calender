class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        vector<int> sum(n+1);
        vector<vector<int>> dp(m+1, vector<int>(n+1, INT_MAX));
        int i = 0, j = 0, k = 0;
        for (i = 1; i <= n; ++i) sum[i] = sum[i-1] + nums[i-1];
        for (i = 0; i <= m; ++i) dp[i][0] = 0;
        
        for (i = 1; i <= m; ++i) {
            for (j = 1; j <= n; ++j) {
                for (k = i-1; k < j; ++k) {
                    int tmp = max(dp[i-1][k], sum[j] - sum[k]);
                    dp[i][j] = min(dp[i][j], tmp);
                }
            }
        }
        
        return dp[m][n];
    }
};
