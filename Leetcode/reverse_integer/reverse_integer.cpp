#include <bits/stdc++.h>
using namespace std;

// Process for reversing an int
// 123 -> "123" -> [3,2,1] -> validate number is within 32bit limit -> 0 | "321" -> 321;
class Solution {
public:
    int reverse(int x) {
        // Convert number to str and reverse it
        string reverse = to_string(x);
        if (reverse[0] == '-') {
            reverse.erase(0, 1);
        }
        std::reverse(reverse.begin(), reverse.end());
        
        // Check if number is in the billions
        if (reverse.size() > 9) {
            // Check if reversed number is >= 3b
            if (reverse[0] > '2') { return 0;}
            
            // set to min or max of 32bit int depending on original numbers sign
            int maxval = INT32_MAX;
            if ((x < 0) - (x > 0)) {maxval =INT32_MIN;}
            string maxvalue = to_string(maxval);
            if (maxvalue[0] == '-') {maxvalue.erase(0, 1);}
            
            // Check if any value exceeds max value
            for (int i = 0; i < maxvalue.size(); i++) {
                if (maxvalue[i] > reverse[i]) {
                    break;
                } else if(reverse[i] > maxvalue[i]) {
                    return 0;
                }
            }
        } 
        
        int finalnum = stoi(string(reverse.begin(), reverse.end()));
        finalnum = x < 0 ? finalnum*-1 : finalnum;

        return finalnum;
    }
};


int main(int argc, char** argv) {
    Solution s;
    cout << s.reverse(-2147483412) << endl;
    cout << s.reverse(1563847412) << endl;
    cout << (s.reverse(-2147483412) == -2143847412) << endl;
    return 0;
}