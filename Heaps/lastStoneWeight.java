
import java.util.*; 
class Solution{
  public static int lastStoneWeight(int[] stones){
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

    for (int stone : stones) {
      maxHeap.add(stone); 
    }

    while (maxHeap.size() > 1){
      int a = maxHeap.poll(); 
      int b = maxHeap.poll(); 

      maxHeap.add(a-b); 
    }

    return maxHeap.peek(); 
  }
  public static void main(String[] args) {
      int[] stones = {2,7,4,1,8,1} ;
      System.out.println(lastStoneWeight(stones)); 
  }
}