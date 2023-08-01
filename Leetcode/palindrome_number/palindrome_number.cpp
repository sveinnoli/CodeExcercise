class Solution {
public:
    bool isPalindrome(int x) {
        long reversed = 0;
        int remainder, temp = x;
        if (x < 0) {
            return false;
        }
        while (x != 0) {
            remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        return reversed == temp;
    }
};
