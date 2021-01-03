class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0) return 0;

        long b = n;
        if (b < 0) {
            x = 1/x;
            b = -b;
        }

        double res = 1.0;
        while(b != 0) {
            if (b & 1) {
                res = res*x;
            }
            x = x*x;
            b = b >> 1;
        }
        return res;
    }
};
