class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        int n = matrix.size(), m = matrix[0].size();

        int i = n-1, j = 0;

        while (i >= 0 && j < m) {
            if (matrix[i][j] == target) return true;
            else if (matrix[i][j] < target) ++j;
            else --i;
        }

        return false;
    }
};
