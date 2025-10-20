# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# Example 1:
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.

# Example 2:
# Input: arr = [11,81,94,43,3]
# Output: 444

def sumSubarrayMins(arr):
        MOD = 10**9 + 7 
        n = len(arr)
        left = [0]*n
        right = [0]*n

        stack = []
        for i in range(n): 
            while stack and arr[stack[-1]] >= arr[i]: 
                stack.pop()
            if not stack : 
                prev_less_index = -1
            else : 
                prev_less_index = stack[-1]
            
            left[i] = i - prev_less_index 
            stack.append(i)

        stack = [] 
        for i in range(n-1,-1,-1): 
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()
            if not stack : 
                next_less_index = n
            else : 
                next_less_index = stack[-1]
            
            right[i] = next_less_index - i 
            stack.append(i)

    
        total = 0 
        for i in range(n): 
            total = (total + left[i] * right[i] * arr[i])%MOD 
        
        return total 