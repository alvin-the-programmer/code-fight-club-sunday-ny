class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
        if l1 is None and l2 is None:
          if carry == 1:
            return ListNode(1)
          else:
            return None

        val1 = 0 if l1 is None else l1.val
        val2 = 0 if l2 is None else l2.val

        next1 = l1.next if l1 is not None else None
        next2 = l2.next if l2 is not None else None
        addition = val1 + val2 + carry
        next_carry = 0

        if addition >= 10:
            next_carry = 1
            addition -= 10

        result_node = ListNode(addition)
        result_node.next = self.addTwoNumbers(next1, next2, next_carry)
        return result_node
      
    def _addTwoNumbers_noEdgeCases(self, l1, l2):
      if l1 is None and l2 is None:
        return None
        # add the two numbers together and make a new node with that value
      result_node = ListNode(l1.val + l2.val)
      # recursive call with the next value of both linked lists
      result_node.next = self.addTwoNumbers(l1.next, l2.next)
      return result_node

    def _addTwoNumbers_differentLinkedListLengths(self, l1, l2):
      if l1 is None and l2 is None:
        return None
      # Set the value to 0 if there is no number to add
      val1 = 0 if l1 is None else l1.val
      val2 = 0 if l2 is None else l2.val
      # Don't proceed to next if there is no next
      next1 = l1.next if l1 is not None else None
      next2 = l2.next if l2 is not None else None

      result_node = ListNode(val1 + val2)
      result_node.next = self.addTwoNumbers(next1, next2)
      return result_node

    # account for the carry
    def _addTwoNumbers_accountForSimpleCarry(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
      if l1 is None and l2 is None:
        return None

      val1 = 0 if l1 is None else l1.val
      val2 = 0 if l2 is None else l2.val

      next1 = l1.next if l1 is not None else None
      next2 = l2.next if l2 is not None else None
      # account for when the sum is greater or equal to 10
      addition = val1 + val2 + carry
      next_carry = 0
      if addition >= 10:
          next_carry = 1
          addition -= 10

      result_node = ListNode(addition)
      # pass the next carry on
      result_node.next = self.addTwoNumbers(next1, next2, next_carry)
      return result_node

# a = ListNode('a')
# b = ListNode('b')
# c = ListNode('c')

# a.next = b
# b.next = c

# print(a.val)
# print(a.next.val)
# print(a.next.next.val)
# print(a.next.next.next)
