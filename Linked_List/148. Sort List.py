# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution: 
  def sortList(self,head): 
    if not head or not head.next : 
      return head 
    
    slow , fast = head , head.next 
    while fast and fast.next: 
      slow = slow.next 
      fast = fast.next.next 
      
    mid = slow.next 
    slow.next = None
    
    left = self.sortList(head)
    right = self.sortList(mid)
    return self.merge(left,right)
  
  def merge(self,left,right): 
    dummy = ListNode(0)
    current = dummy.next
    
    while left and right : 
      if left.val < right.val : 
        current.next = left
        left = left.next 
      else : 
        current.next = right
        right = right.next 
      current = current.next 
    
    if left: current.next = left
    if right: current.next = right
    return dummy.next  

