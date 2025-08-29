# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

def myPow(x, n):
        if n < 0 : 
            x = 1/x 
            n = -n 

        result = 1 
        while n > 0 : 
            if n % 2 == 1 : 
                result*=x 
            x*=x 
            n//=2
        return result
      
print(myPow(2,10))

# Example: 
# x=2
# n=10

# Start: result = 1, x = 2, n = 10

# Step 1: n even → result = 1, x = 4, n = 5

# Step 2: n odd → result = 1*4 = 4, x = 16, n = 2

# Step 3: n even → result = 4, x = 256, n = 1

# Step 4: n odd → result = 4*256 = 1024, x = 65536, n = 0

# Done → Answer = 1024 ✅