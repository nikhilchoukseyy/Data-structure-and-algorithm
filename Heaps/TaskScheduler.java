import java.util.*; 

class TaskScheduler {
  public static int TaskScheduler(char[] tasks , int n ){
    int[] freq = new int[26]; 

    for (char t : tasks){ //frequency array
      freq[t-'A']++; 
    }

    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverse()); 

    for (int f : freq){
      if (f > 0) maxHeap.add(f); 
    }

    int time = 0 ; 

    while (!maxHeap.isEmpty()){
      List<Integer> temp = new ArrayList<>(); 

      int cycle = n + 1 ; 

      while (cycle > 0 && !maxHeap.isEmpty()){
        int count = maxHeap.poll();

        if (count-1  > 0 ){
          temp.add(count -1); 
        }
        time++ ; 
        cycle-- ; 

      }

      for(int remaining : temp){  //add remaining freq in maxHeap 
        maxHeap.add(remaining);
      }


      //if maxHeap is not empty means tasks is reamining , so add cycle or idle time in time
      if (!maxHeap.isEmpty()){ 
        time += cycle ; 
      }
    }
    return time ; 
  }

  public static void main(String[] args) {
      char[] tasks = {'A','A','A','B','B','B'} ;

      int n = 2 ; 

      System.out.println(TaskScheduler(tasks, n)); 
  }
}