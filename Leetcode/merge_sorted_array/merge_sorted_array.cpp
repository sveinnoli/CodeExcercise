#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i = m; i < m+n; i++) {
            nums1[i] = nums2[i-m];
        }
        sort(nums1.begin(), nums1.end());
    }
};

int main() {
    Solution s = Solution();
    vector<int> v1 = {1,2,3};
    v1.resize(6);
    vector<int> v2 = {5, 9, 10};
    s.merge(v1, 3, v2, 3);
    return 0;
}