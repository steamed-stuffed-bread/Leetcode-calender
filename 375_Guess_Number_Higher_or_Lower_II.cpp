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

// Back Tracing
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int res = 1, max = pow(10, n), used = 0;
        for (int i = 1; i < 10; ++i) {
            used |= (1 << i);
            res += search(i, max, used);
            used &= ~(1 << i);
        }
        return res;
    }
    
    int search(int pre, int max, int& used) {
        int res = 0;
        if (pre < max) res++;
        else return res;
        
        for (int i = 0; i < 10; ++i) {
            if (!(used & (1 << i))) {
                used |= (1 << i);
                int cur = pre*10 + i;
                res += search(cur, max, used);
                used &= ~(1 << i);
            }
        }
        
        return res;
    }
};
