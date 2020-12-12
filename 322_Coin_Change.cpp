class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, amount+1);
        dp[0] = 0;
        
        for (int i = 0; i <= amount; ++i) {
            for (int j = 0; j < coins.size(); ++j) {
                if (coins[j] <= i) {
                    dp[i] = min(dp[i-coins[j]] + 1, dp[i]);
                }
            }
        }
        return dp[amount] > amount?-1:dp[amount];
    }
};

// Brute Force
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size(), res = INT_MAX;
        sort(coins.begin(), coins.end());
        helper(coins, amount, n-1, 0, res);
        return (res == INT_MAX)?-1:res;
    }
    
    void helper(vector<int>& coins, int t, int start, int cur, int& res) {
        if (start < 0) return;
        if (t%coins[start] == 0) {
            res = min(res, cur + t/coins[start]);
            return;
        }
        
        for (int i = t/coins[start]; i >= 0; --i) {
            if (cur + i >= res -1) break;
            helper(coins, t-coins[start]*i, start-1, cur+i, res);
        }
    }
};
