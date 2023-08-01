#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    string alternate_string(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        string alt;
        for (int i = 0; i < min(n,m); i++) {
            alt.push_back(word1[i]);
            alt.push_back(word2[i]);
        }
        const auto& biggest = n > m ? word1 : word2;
        for (int i = min(n,m); i < biggest.size(); i++) {
            alt.push_back(biggest[i]);
        }

        return alt;
    }
};

int main(int argc, char** argv) {
    string w1 = "aaaaa";
    string w2 = "bbbbbbbbb";
    Solution s = Solution();
    cout << s.alternate_string(w1, w2);
    return 0;
}

