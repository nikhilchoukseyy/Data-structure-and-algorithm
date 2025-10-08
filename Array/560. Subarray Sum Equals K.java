// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
// A subarray is a contiguous non-empty sequence of elements within an array.

// Example 1:
// Input: nums = [1,1,1], k = 2
// Output: 2

// Example 2:
// Input: nums = [1,2,3], k = 3
// Output: 2

import java.util.*; 

class Solution {
    public int subarraySum(int[] nums, int k) {
        int result = 0 ; 
        int prefSum = 0 ; 
        Map<Integer,Integer> mp = new HashMap<>(); 
        mp.put(0,1); 
        for (int n: nums){
            prefSum += n;  

            if (mp.containsKey(prefSum-k)){
                result += mp.get(prefSum-k) ; 
            } 

            mp.put(prefSum, mp.getOrDefault(prefSum,0)+1); 
        }
        return result;
    }
}