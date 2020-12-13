class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0, j = 0, cur = 0, n = chars.size();
        
        for (i = 0, j = 0; i < n; i = j) {
            while (j < n && chars[i] == chars[j]) ++j;
            chars[cur++] = chars[i];
            if (j - i == 1) continue;
            else {
                for (auto c:to_string(j-i)) chars[cur++] = c;
            }
        }
        
        return cur;
    }
};
