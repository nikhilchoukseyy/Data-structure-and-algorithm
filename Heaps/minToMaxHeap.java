// Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.
// A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in the Binary Tree.
// A max-heap is a complete binary tree where the key at the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in the Binary Tree.
// Since there can be multiple answers, the compiler will return true if it's correct, else false.


// Examples:
// Input: nums = [10, 20, 30, 21, 23]
// Output: [30, 21, 23, 10, 20]
// Explanation:

// Input: nums = [-5, -4, -3, -2, -1]
// Output: [-1, -2, -3, -4, -5]
// Explanation:

import java.util.* ; 

class minToMaxHeap{
  public static void convert(int[] arr){
    int n = arr.length ; 
    
    for (int i = (n/2)-1 ; i >= 0 ; i--){
      Heapify(arr, i, n);
    }
  }

  public static void Heapify(int[]arr , int i , int n){
    int largest = i ; 
    int left = 2*i + 1; 
    int right = 2*i + 2 ; 


    if (left < n && arr[left] > arr[largest]) {
      largest = left; 
      } 
    if (right < n && arr[right] > arr[largest]){
      largest = right; 
    }
    if (largest != i){
      int temp = arr[i]; 
      arr[i] = arr[largest]; 
      arr[largest] = temp ; 
      Heapify(arr, largest, n);
    }
  }

  public static void main(String[] args) {
      int[] arr = {1,3,5,7,9,6} ; 
      
      convert(arr); 

      System.out.println(Arrays.toString(arr)); 
  }
}