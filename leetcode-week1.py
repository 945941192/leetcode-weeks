
# 66. plus-one
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] %= 10
        return [1] + digits

# 21. merge-two-sorted-lists 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

