class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.size(), n = b.size();
        string res = "";
        int i = m-1, j = n-1, cnt = 0;
        while (i >= 0 || j >= 0) {
            int t1 = (i >= 0)?a[i--]-'0':0;
            int t2 = (j >= 0)?b[j--]-'0':0;
            
            int tmp = t1+t2+cnt;
            res.insert(0, to_string(tmp%2));
            cnt = tmp/2;
        }
        
        if (cnt) res.insert(0, to_string(cnt));
        return res;
    }
};
