class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.empty()) return 0;
        vector<int> g(k+1, 0);
        vector<int> l(k+1, 0);
        int diff = 0;
        for (int i = 1; i < prices.size(); ++i) {
            diff = prices[i] - prices[i-1];
            for (int j = k; j > 0; j--) {
                l[j] = max(g[j-1] + max(diff, 0), l[j] + diff);
                g[j] = max(g[j], l[j]);
            }
        }
        return g[k];
    }
};
