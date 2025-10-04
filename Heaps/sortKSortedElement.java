// A nearly sorted (or k-sorted) array means:
// Each element is at most k positions away from its correct sorted position.

// Example:
// arr = [6, 5, 3, 2, 8, 10, 9],  k = 3
// The sorted array is: [2, 3, 5, 6, 8, 9, 10]
// 6 is at index 0, but its correct position is index 3 (moved 3 positions).
// 5 is at index 1, correct index is 2 (moved 1 position).etc.
// ✅ So, we can solve this faster than normal O(n log n) sorting by using a min-heap of size k+1.


import java.util.* ; 

class Solution { 
  public static void sortKSortedArray(int[] arr ,int k ){
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(); 
    
    int n = arr.length ; 
    int index = 0 ; 

    for (int a : arr){
      minHeap.add(a); 

      if (index < n && minHeap.size() > k ){
        arr[index] = minHeap.poll(); 
        index ++ ; 
      } 
    }

    while(!minHeap.isEmpty() && index < n ){
      arr[index] = minHeap.poll(); 
      index ++ ; 
    }
  }

  public static void main(String[] args) {
      int[] arr = {6, 5, 3, 2, 8, 10, 9} ; 
      int k = 3 ; 
      sortKSortedArray(arr,k); 
      System.out.println(Arrays.toString(arr)); 
  }
}