// Problem 25: Reverse Nodes in k-Group
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        
        // Check if we have at least k nodes
        ListNode* curr = head;
        for (int i = 0; i < k; i++) {
            if (!curr) return head; // Less than k nodes, return as is
            curr = curr->next;
        }
        
        // Reverse first k nodes
        ListNode* prev = nullptr;
        curr = head;
        for (int i = 0; i < k; i++) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        
        // Recursively reverse remaining groups
        head->next = reverseKGroup(curr, k);
        
        return prev; // New head of this group
    }
};

// Alternative iterative solution for Problem 25
class SolutionIterative {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prevGroupEnd = &dummy;
        
        while (true) {
            // Check if we have k nodes to reverse
            ListNode* kthNode = prevGroupEnd;
            for (int i = 0; i < k && kthNode; i++) {
                kthNode = kthNode->next;
            }
            if (!kthNode) break;
            
            ListNode* nextGroupStart = kthNode->next;
            
            // Reverse k nodes
            ListNode* prev = nextGroupStart;
            ListNode* curr = prevGroupEnd->next;
            
            while (curr != nextGroupStart) {
                ListNode* next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
            
            // Connect with previous group
            ListNode* temp = prevGroupEnd->next;
            prevGroupEnd->next = kthNode;
            prevGroupEnd = temp;
        }
        
        return dummy.next;
    }
};

// Problem 23: Merge k Sorted Lists
class MergeSolution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        return divideAndConquer(lists, 0, lists.size() - 1);
    }
    
private:
    ListNode* divideAndConquer(vector<ListNode*>& lists, int start, int end) {
        if (start == end) return lists[start];
        if (start > end) return nullptr;
        
        int mid = start + (end - start) / 2;
        ListNode* left = divideAndConquer(lists, start, mid);
        ListNode* right = divideAndConquer(lists, mid + 1, end);
        
        return mergeTwoLists(left, right);
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        
        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};

// Alternative Priority Queue solution for Problem 23
class MergeSolutionPQ {
public:
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // Min heap
        }
    };
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
        
        // Add first node of each list to priority queue
        for (ListNode* list : lists) {
            if (list) pq.push(list);
        }
        
        ListNode dummy(0);
        ListNode* tail = &dummy;
        
        while (!pq.empty()) {
            ListNode* smallest = pq.top();
            pq.pop();
            
            tail->next = smallest;
            tail = tail->next;
            
            if (smallest->next) {
                pq.push(smallest->next);
            }
        }
        
        return dummy.next;
    }
};