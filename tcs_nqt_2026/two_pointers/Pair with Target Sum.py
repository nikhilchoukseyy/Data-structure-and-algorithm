# Given a sorted array of N integers and an integer K, print the 1-based indices of the pair whose sum is exactly K.

# If multiple answers exist, print the pair with the minimum first index.

# If no such pair exists print -1.

# Input
# 7
# 1 2 3 4 4 7 10
# 8
# Output
# 1 6

# Tests

# Input
# 6
# 1 3 5 7 8 10
# 13

# Output
# 2 5


def solve(): 
    n = int(input())
    nums = list(map(int,input().split()))
    target = int(input())
    left , right = 0 , n-1 
    while left < right : 
        sum = nums[left] + nums[right] 
        if sum == target : 
            return [left+1,right+1] 
        elif sum < target : 
            left += 1
        else : 
            right -= 1 
    return [-1]


print(*solve())