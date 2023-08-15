// https://leetcode.com/problems/subarray-sum-equals-k/
#include <vector>
#include <iostream>

using namespace std;
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        return k;
    }
};


int main(int argc, char** argv) {
    Solution s;    
    vector<int> v = {1,2,3};
    cout << s.subarraySum(v, 3);
    return 0;
}