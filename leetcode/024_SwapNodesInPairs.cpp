#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class List {
    ListNode *head;
public:
    void outputList() {
        ListNode *cur = head;
        while (cur != NULL) {
            cout<<cur->val<<"->";
            cur = cur->next;
        }
    }
    void insertList(int x) {
        ListNode node(x);
        ListNode *cur = head;
        if (cur == NULL) { head = &node; return; }
        while (cur->next != NULL) {
            cur = cur->next;
        }
        cur-->next = &node;
    }
    ListNode *getHead() { return head; }
    void updateHead(ListNode *newHead) {
        head = newHead;
    }
};

class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
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
    return 0;
}

