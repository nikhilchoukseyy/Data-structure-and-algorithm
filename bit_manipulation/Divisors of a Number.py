# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.


# A number which completely divides another number is called it's divisor.


# Examples:

# Input: n = 6
# Output = [1, 2, 3, 6]
# Explanation: The divisors of 6 are 1, 2, 3, 6.

# Input: n = 8
# Output: [1, 2, 4, 8]
# Explanation: The divisors of 8 are 1, 2, 4, 8.

def divisors(n):
    small = []
    large = []
    for i in range(1,int(n**0.5) + 1): 
        if n % i == 0 : 
            small.append(i)
            large.append(n//i)
    
    return small + large[::-1]
    
print(divisors(6))

