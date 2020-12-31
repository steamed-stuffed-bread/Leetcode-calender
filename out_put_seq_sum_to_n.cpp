void seq(int n, vector<vector<int>>& res) {
    int s = 1, l = 2;
    while (s <= n/2) {
        int sum = (l-s+1)*(s+l)/2;
        if (sum == n) {
            vector<int> tmp;
            cout << "seq: ";
            for (int i = s; i <= l; ++i) {
                tmp.push_back(i);
                cout << i << " ";
            }
            cout << endl;
            res.push_back(tmp);
            s++;
            l = s+1;
        } else if (sum < n) l++;
        else s++;
    }
}


int main() {
    std::cout << "Hello World!\n";
    vector<vector<int>> res;
    seq(15, res);
}
