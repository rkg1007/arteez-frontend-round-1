# Problem Statement
You are given an N × N matrix in which every cell is colored black or white. Columns are numbered from 0
to N-1 (from left to right). This coloring is represented by a non-empty array of integers A. If the K-th
number in the array is equal to X then the X lowest cells in the K-th column of the matrix are black. The
rest of the cells in the K-th column are white. The task is to calculate the side length of the biggest black
square (a square containing only black cells).Write a function:class Solution { public int solution(int[] A);
}that, given an array of integers A of length N representing the coloring of the matrix, returns the side
length of the biggest black square.

E.g.

- For input arr [1,2,5,3,1,3] answer should be 2
- For input arr [3,3,3,5,4] answer should be 3
- For input arr [6,5,5,6,2,2] answer should be 4

Constraints
- 1 <= N <= 10^5
- 1 <= A[i] <= N

# Solution
We can observe that if assume X is a possible then definitely X-1 will also be a possible answer because if we can make a square with side length X then we can also create a square with smaller side length.
But we can not tell this for X+1. So using this observation, we can apply Binary Search over answer and our answer can lie between 0 to N (size of matrix). Now question becomes how to find where X is a possible answer or not??

To find where X is possible answer or not, we can traverse over given array indexes one by one and check if current index can become left side of square or not which has side length as X. 
For each index `i`, if all the indexes from `i` to `i+X-1` has minimum value X then index `i` can become possible left side of square which has side length as X. Now again our question reduced to 
how to find minimum value between index range `i` to `i+x-1` efficiently???

Now we can find minimum value between index range `i` to `i+x-1` using Segment Tree easily and efficiently.


### How To Run Code
1. Please make sure that Python-3 is installed in  your system.
2. Clone this repository
3. Run python file given in this repository and given space separated integers as input array in the terminal after running the code
