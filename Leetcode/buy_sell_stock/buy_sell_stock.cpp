#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = prices[0];
        int maxprofit = 0;
        for (int i = 1; i < prices.size(); i++) {
            lowest = min(lowest, prices[i]);
            maxprofit = max(maxprofit, prices[i] - lowest);
        }
        return maxprofit;
    }
};


int main() {
    Solution* s = new Solution();
    vector<int> v = vector<int>({7,6,4,3,1});
    cout << s->maxProfit(v);
    return 0;
}