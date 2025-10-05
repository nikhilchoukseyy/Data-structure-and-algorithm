// 347. Top K Frequent Elements
// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// Example 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]

// Example 2:
// Input: nums = [1], k = 1
// Output: [1]

// Example 3:
// Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
// Output: [1,2]


import java.util.* ; 
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freq = new HashMap<>(); 

        for (int num : nums){
            freq.put(num,freq.getOrDefault(num,0)+1); 
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b)->freq.get(b) -freq.get(a)); 

        for (int num : freq.keySet()){
            maxHeap.add(num); 
        }

        int[] result = new int[k];
        for (int i = 0 ; i < k ; i++) {
            result[i] = maxHeap.poll(); 
        }

        return result ; 
    }
}