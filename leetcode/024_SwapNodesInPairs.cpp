#include <iostream>
#include <cstdio>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL) {}
};
/*
class List {
    ListNode* head;
public:
    List(): head(NULL) {}

    void outputList() {
        ListNode* cur = head;
        while (cur != NULL) {
            cout<<cur->val<<"->";
            cur = cur->next;
        }
        cout<<"end"<<endl;
    }

    void insertList(int x) {
        ListNode* node = new ListNode(x);
        if (head == NULL) { head = node; return; }
        ListNode* cur = head;
        while (cur->next != NULL) {
            cur = cur->next;
        }
        cur->next = node;
    }

    ListNode* getHead() { return head; }

    void updateHead(ListNode *newHead) {
        head = newHead;
    }
};
*/
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL) { return head; }
        ListNode* temp = head;
        head = temp->next;
        temp->next = head->next;
        head->next = temp;

        if (temp->next != NULL) {
            temp->next = swapPairs(temp->next);
        }
        return head;
    }
};

/*
int main() {
    Solution a;
    List list;
    list.insertList(1);
    list.insertList(2);
    list.insertList(3);
    list.insertList(4);
    list.outputList();
    list.updateHead(a.swapPairs(list.getHead()));
    list.outputList();
    getchar();
    return 0;
}
*/