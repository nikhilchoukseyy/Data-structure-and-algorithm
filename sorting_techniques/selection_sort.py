# For each i, you find the index of the smallest element in the rest of the array.

# Swap once at the end of the inner loop.

# This guarantees only 1 swap per pass (at most n-1 swaps total).


def selectionSort(nums):
    n = len(nums)
    for i in range(n): 
      min_index = i
      for j in range(i+1,n): 
        if nums[min_index] > nums[j] : 
            min_index = j 
      nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums

nums = [7,3,1,2,5]
print(selectionSort(nums))