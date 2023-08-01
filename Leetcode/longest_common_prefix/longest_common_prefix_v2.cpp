#include <bits/stdc++.h>
using namespace std;

// Works but it only works because it compares out-of-bounds memory with a valid string or another out-of-bound memory check
// And it will eventually access out-of-bounds memory which has a high unlikelyhood of being the same character as the
// one being compared in strs[j][i] != strs[j+1][i]
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        string output;
        for(int i = 0; i < strs[0].size(); i++) {
            for(int j = 0; j < n-1; j++) {
                if(strs[j][i] != strs[j+1][i]) {
                    return output;
                }
            }
            output.push_back(strs[0][i]);
        }
        return output;
    }
};


int main(int argc, char** argv) {
    Solution s;
    vector<string> v;
    v.push_back("aa");
    v.push_back("a");
    cout << s.longestCommonPrefix(v);
    return 0;
}