// Given an m x n matrix, return all elements of the matrix in spiral order.

// Example 1:
// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]

// Example 2:
// Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution {
  public static List<Integer> SpiralMatrix(int[][] matrix){
    int m = matrix.length; 
    int n = matrix[0].length ; 

    int top = 0 ; 
    int bottom = m-1 ; 
    int left = 0 ; 
    int right = n-1 ; 

    int dir = 0 ; 

    List<Integer> result = new ArrayList<>(); 

    while (top<= bottom && left <= right){
      if (dir == 0){
        for(int i = left ; i <= right ; i++){
          result.add(matrix[top][i]); 
        }
        top++; 
      }
      if (dir == 1 ){
        for(int i = top ; i <= down ; i++){
          result.add(matrix[i][right]); 
        }
        right -- ; 
      }
      if (dir == 2){
        for(int i = right ; i >= left ; i--){
          result.add(matrix[bottom][i]); 
        }
        bottom --; 
      }
      if (dir == 3){
        for(int i = bottom ; i >= top ; i--){
          result.add(matrix[i][left]); 
        }
        left++; 
      }
      dir++; 

      if (dir > 3){
        dir = 0 ; 
      }
    }
    return result ; 
  }
}