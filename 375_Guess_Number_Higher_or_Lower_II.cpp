class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> m(n+1, vector<int>(n+1,0));
        return helper(1, n, m);
    }
    
    int helper(int start, int end, vector<vector<int>>& m) {
        if (start >= end) return 0;
        if (m[start][end] > 0) return m[start][end];
        
        int res = INT_MAX;
        for (int i = start; i <= end; ++i) {
            int t = i + max(helper(start, i-1, m), helper(i+1, end, m));
            res = min(res, t);
        }
        
        m[start][end] = res;
        return m[start][end];
    }
};
