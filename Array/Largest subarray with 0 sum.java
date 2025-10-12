// Given an array arr[] containing both positive and negative integers, the task is to find the length of the longest subarray with a sum equals to 0.

// Note: A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

// Examples:
// Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
// Output: 5
// Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].

// Input: arr[] = [2, 10, 4]
// Output: 0
// Explanation: There is no subarray with a sum of 0.

// Input: arr[] = [1, 0, -4, 3, 1, 0]
// Output: 5
// Explanation: The longest subarray with sum equals to 0 is [0, -4, 3, 1, 0]

import java.util.*; 
class Solution {
    int maxLength(int arr[]) {
        // code here
        int maxLen = 0 ; 
        int prefSum = 0 ; 
        
        HashMap<Integer,Integer> prefMap = new HashMap<>(); 
        
        for(int i = 0 ; i < arr.length ; i++){
            prefSum += arr[i];
            
            if (prefSum == 0 ){
                maxLen = i+1; 
            }
            
            if(prefMap.containsKey(prefSum)){
                maxLen = Math.max(maxLen,i-prefMap.get(prefSum)); 
            }else{
                prefMap.put(prefSum,i);
            } 
            
        }
        
        return maxLen ; 
    }
}