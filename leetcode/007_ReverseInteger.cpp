/*
#include <cstdio>
#include <iostream>
#include <climits>
#include <cmath>
using namespace std;
*/

class Solution {
public:
    int reverse(int intx) {
        int oper = intx >= 0 ? 1 : -1;
        long x = abs((long)intx);
        long res = 0;
        while (x >= 10) {
            
            res = res * 10 + x % 10;
            x = x / 10;
            //cout<<"res="<<res<<" x="<<x<<endl;
        }
        res = res * 10 + x;
        return res > INT_MAX ? 0 : oper * res;
    }
};

/*
int main(){
    Solution a;
    cout<<a.reverse(-2147483648)<<endl;
    cout<<a.reverse(-1024)<<endl;
    getchar();
    return 0;
}
*/