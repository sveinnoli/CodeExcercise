#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int uniquecount = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i+1]) {
                nums[uniquecount++] = nums[i];
            }
        }

        return uniquecount;
    }
};


int main(int argc, char** argv) {
    Solution s;
    vector<int> v = {1};
    
    cout << s.removeDuplicates(v) << " ";
    for (int i : v) {
        cout << i << " ";
    }

    return 0;

}