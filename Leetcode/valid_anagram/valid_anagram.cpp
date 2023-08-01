#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<int, int> charCount;
        
        for (char c : s) {
            charCount[c]++;
        }   

        for (char c : t) {
            charCount[c]--;
            if (charCount[c] < 0) {
                return false;
            }
        }

        for (const auto& pair : charCount) {
            if (pair.second != 0) {
                return false;
            }
        }

        return true;
    }
};


int main(int argc, char** argv) {
    Solution s;
    bool r = s.isAnagram(std::string("aacc"), std::string("ccaa"));
    cout << r;
    return 0;
}