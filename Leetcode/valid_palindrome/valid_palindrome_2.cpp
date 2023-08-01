#include <string>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int right = s.length()-1;
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        for (int left = 0; left < right;) {
            
            if (isalnum(s[left])) {
                if (isalnum(s[right])) {
                    if (s[left] != s[right]) {
                        return false;
                    }
                    left++;
                    right--;
                } else {
                    while (left < right && !isalnum(s[right])) right--;
                }
            } else {
                while (left < right && !isalnum(s[left])) left++;
            }
        }
        return true;      
    }
};


int main(int argc, char** argv) {
    Solution s;
    bool r = s.isPalindrome(std::string("A man, a plan, a canal: Panama"));
    cout << r;
    return 0;
}