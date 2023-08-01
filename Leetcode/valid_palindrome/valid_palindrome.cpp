#include <string>
#include <regex>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        std::regex pattern("[\\W_]");
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        s=regex_replace(s, pattern, "");
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != s[s.length() - i - 1]) {
                return false;
            }
        }
        return true;
    }
};


int main(int argc, char** argv) {
   Solution s;
   bool r = s.isPalindrome(std::string("H L e l H")); 
   cout << r;
    return 0;
}