#include <vector>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1;
        int j=n-1;
        int k=m+n-1;

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
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