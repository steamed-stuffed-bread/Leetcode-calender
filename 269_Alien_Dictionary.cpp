class Solution {
public:
    string alienOrder(vector<string>& words) {
        string res = "";
        set<pair<char, char>> st;
        unordered_set<char> d;
        queue<char> q;
        vector<int> in(256);
        int i = 0, j = 0;
        for (auto w:words) d.insert(w.begin(), w.end());
        for (i = 0; i < words.size()-1; ++i) {
            int mn = min(words[i].size(), words[i+1].size());
            for (j = 0; j < mn; ++j) {
                if (words[i][j] != words[i+1][j]) {
                    st.insert(make_pair(words[i][j], words[i+1][j]));
                    break;
                }
            }
            if (j == mn && words[i].size() > words[i+1].size()) return "";
        }
        
        for (auto p:st) in[p.second] += 1;
        for (auto c:d) {
            if (in[c] == 0) {
                q.push(c);
                res += c;
            }
        }
        
        while (!q.empty()) {
            char tmp = q.front(); q.pop();
            for (auto pair:st) {
                if (pair.first != tmp) continue;
                in[pair.second] -= 1;
                if (in[pair.second] == 0) {
                    q.push(pair.second);
                    res += pair.second;
                }
            }
        }
        
        return res.size() == d.size() ? res: "";
    }
};
