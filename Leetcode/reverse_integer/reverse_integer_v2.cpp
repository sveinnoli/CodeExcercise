#include <bits/stdc++.h>
using namespace std;

class Solution {
public: 
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int remainder = x % 10;
            x /= 10;
            if (rev > INT32_MAX/10 || rev == INT32_MAX/10 && remainder > 7) {return 0;}
            if (rev < INT32_MIN/10 || rev == INT32_MIN/10 && remainder < -8) {return 0;}
            rev = rev * 10 + remainder;
        }
        return rev;
    }
};

int main(int argc, char** argv) {
    Solution s;
    cout << s.reverse(-2147483412) << endl;
    cout << s.reverse(1563847412) << endl;
    cout << (s.reverse(-2147483412) == -2143847412) << endl;
    return 0;
}

