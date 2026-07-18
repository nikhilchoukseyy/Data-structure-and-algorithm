# Given
# nums = [10,4,8,20,2]
# Print the smallest element using a heap.
# Expected Output
# 2

import heapq 

def k_smallest_element(): 
  nums = list(map(int,input().split()))
  heap = []
  for num in nums : 
    heapq.heappush(heap,num)

  return heap[0]

print(k_smallest_element())