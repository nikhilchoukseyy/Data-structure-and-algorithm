# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5

def getSum(a,b):
        carry = 0 
        result = 0 
        for i in range(32): 
            bit_mask = (1<<i)
            abit = 1 if (bit_mask & a) else 0 
            bbit = 1 if (bit_mask & b) else 0 

            total = abit + bbit + carry 

            if total % 2 == 1 : 
                result |= bit_mask
            
            carry = 1 if total >= 2 else 0 
        
        if result >= (1 << 31):
            result -= (1 << 32)

        return result
      
print(getSum(5,3))