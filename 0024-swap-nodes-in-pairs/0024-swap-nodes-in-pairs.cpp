class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // Edge case: empty or single node
        if (!head || !head->next) return head;

        // Dummy node to simplify swapping head pairs
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        while (prev->next && prev->next->next) {
            ListNode* first = prev->next;
            ListNode* second = first->next;

            // Perform the swap
            first->next = second->next;
            second->next = first;
            prev->next = second;

            // Move prev pointer two nodes ahead for next swap
            prev = first;
        }

        return dummy.next;
    }
};
