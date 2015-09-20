/*
#include <cstdio>
#include <iostream>
#include <climits>
#include <string>
using namespace std;
*/

class Solution {
public:
    int myAtoi(string str) {
        long res = 0;
        int oper = 1;
        const char* p = str.c_str();
        if (p == NULL) {
            cout<<"This is a NULL string."<<endl;
            return 0;
        }
        while (isspace(*p)) { p++; }
        if (*p == '-') { oper = -1; p++; }
        else if (*p == '+') { p++; }
        if (*p < '0' or *p > '9') { return 0; }
        while (*p >= '0' and *p <= '9') {
            res = res * 10 + (*p - '0');
            if (oper == 1 and res > INT_MAX) {return INT_MAX;}
            if (oper == -1 and -res < INT_MIN) {return INT_MIN;}
            p++;
        }
        return res == 0 ? 0 : oper * res;
    }
};

/*
int main(){
    Solution a;
    cout<<INT_MIN<<endl;
    cout<<a.myAtoi("-123")<<endl;
    cout<<a.myAtoi("-2147483648")<<endl;
    cout<<a.myAtoi("ab-a-13")<<endl;
    getchar();
    return 0;
}
*/