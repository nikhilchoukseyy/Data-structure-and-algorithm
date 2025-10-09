// Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
// Note: A subarray is a continuous part of an array.

// Examples:
// Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
// Output: 11
// Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

// Input: arr[] = [-2, -4]
// Output: -2
// Explanation: The subarray [-2] has the largest sum -2.

// Input: arr[] = [5, 4, 1, 7, 8]
// Output: 25
// Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
class Solution{
  public static int MaxSumSubarray(int[] nums){
    int maxSum =  nums[0]; 
    int currentSum = nums[0] ; 

    for (int i = 0 ; i < nums.length ; i++){
      currentSum = Math.max(currentSum+nums[i] , nums[i]); 
      maxSum = Math.max(currentSum, maxSum) ; 

    }

    return maxSum; 
  }

  public static void main(String[] args) {
      int[] nums = {2, 3, -8, 7, -1, 2, 3} ; 
      System.out.println("Max sum is : " + MaxSumSubarray(nums)); 
  }
}