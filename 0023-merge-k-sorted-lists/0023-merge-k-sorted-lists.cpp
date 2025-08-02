#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // min-heap
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap;

        // Initialize the heap with the head of each non-empty list
        for (auto list : lists) {
            if (list) {
                minHeap.push(list);
            }
        }

        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (!minHeap.empty()) {
            ListNode* smallest = minHeap.top();
            minHeap.pop();

            tail->next = smallest;
            tail = tail->next;

            if (smallest->next) {
                minHeap.push(smallest->next);
            }
        }

        return dummy.next;
    }
};
