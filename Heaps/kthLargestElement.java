
import java.util.*;

class kthLargestElement {

    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int n = nums.length;

        for (int i = 0; i < n; i++) {
            pq.add(nums[i]);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        return pq.peek();
    }

    public static void main(String[] args) {
      int[] nums = {3,2,1,5,6,4};
        int k = 2;
        System.out.println("Kth largest element is: " + findKthLargest(nums, k));
    }
}

