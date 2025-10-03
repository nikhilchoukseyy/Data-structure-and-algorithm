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