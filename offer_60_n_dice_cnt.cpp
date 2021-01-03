class Solution {
public:
    vector<double> dicesProbability(int n) {
        if (n <= 0) return vector<double> ();
        int c = 6, i = 0, j = 0, k = 0, flag = 0;
        vector<vector<int>> count(2, vector<int>(c*n+1, 0));
        for (i = 1; i <= c; ++i) count[flag][i] = 1;
        for (i = 2; i <= n; ++i) {
            for (j = 1; j < i; ++j) count[1-flag][j] = 0;
            for (j = i; j <= c*i; ++j) {
                count[1-flag][j] = 0;
                for (k = 1; k <= 6 && j-k >= 1; k++) {
                    count[1-flag][j] += count[flag][j-k];
                }
            }
            flag = 1-flag;
        }
        double base = pow(c, n);
        vector<double> res(5*n + 1);
        for (i = 0; i < 5*n + 1; ++i) {
            res[i] = count[flag][n+i]/base;
        }
        return res;
    }
};
