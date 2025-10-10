// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

// Example 1:
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

// Example 2:
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9

// Example 3:
// Input: nums = [1,0,1,2]
// Output: 3

import java.util.* ; 
class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length ; 

        if( n == 0 ) {
            return 0; 
        } 

        HashSet<Integer> set = new HashSet<>(); 

        for(int num : nums){
            set.add(num); 
        }

        int maxLen = 0 ; 
        for(int element : set){
            int prevEl = element - 1 ;
            if(!set.contains(prevEl)) { 
                int len = 1 ;
                int nextEl = element + 1; 
                while(set.contains(nextEl)){
                    len++ ;
                    nextEl++; 
                }
                maxLen = Math.max(len,maxLen); 
            }
            
            
        }

        return maxLen;
    }
}