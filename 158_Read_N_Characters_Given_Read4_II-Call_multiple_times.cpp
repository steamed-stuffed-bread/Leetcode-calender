/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int i = 0;
        for (i = 0; i < n; ++i) {
            if (rp == wp) {
                wp = read4(buf4);
                rp = 0;
                if (wp == 0) return i;
                
            }
            buf[i] = buf4[rp++];
        }
        return n;
    }
private:
    int rp = 0, wp = 0;
    char buf4[4];
};
