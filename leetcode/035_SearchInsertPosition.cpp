/*
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
*/
class Solution{
public:
    int searchInsert(vector<int>& nums, int target) {
        return search(nums, target, 0, nums.size() - 1);
        }

    int search(vector<int>& nums, int target, int l, int r) {
        if (l == r) { return target <= nums[l] ? l : l + 1;}
        int m = (l + r) / 2;
        if (target <= nums[m]) { return search(nums, target, l, m);}
        else {return search(nums, target, m + 1, r);}
    }
};

/*
int main(){
    int test[7] = {1,2,3,4,5,9,8};
    //cout<<*(test+6)<<endl;
    vector<int> nums(test, test+6);
    Solution a;
    cout<<a.searchInsert(nums, 3);
    getchar();
}
*/

