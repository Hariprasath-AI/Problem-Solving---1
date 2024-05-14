# Problem-Solving---1
# Problem Description
Assume the variables A and B, where each of the variables ranges from 1 to N. Return the possible pairs count if the total sum(A + B) is equal to N and A < B.
# Input format
Any integer greater than zero
# Output format
Returns total possible pair count
# Sample Input 1
10
# Sample Output 1
4
# Sample Input 2
9
# Sample Output 2
4
# Explanation 1
1) First we have to see all the possible pair, <br/>
   (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10), <br/>
   (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9), (2,10), <br/>
   (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9), (3,10), <br/>
   (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9), (4,10), <br/>
   (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10), <br/>
   (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10), <br/>
   (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9), (7,10), <br/>
   (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), <br/>
   (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9), (9,10), <br/>
   (10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),(10,10) <br/>

2) Out of all possible pairs, the possible sum(A + B = N) pairs are, <br/>
   (1,9) <br/>
   (2,8) <br/>
   (3,7) <br/>
   (4,6) <br/>
   (5,5) <br/>
   (6,4) <br/>
   (7,3) <br/>
   (8,2) <br/>
   (9,1) <br/>

3) From the above possible sum pairs, we need pairs of A < B. So the pairs are, <br/>
   (1,9) <br/> 
   (2,8) <br/>
   (3,7) <br/>
   (4,6) <br/>

4) So above 4 pairs are the pairs that satisfies the problem statement. So the answer is 4.

# 1) Traditional Approach:

  ## PYTHON CODE
  N, count = int(input()),0 <br/>
  for i in range(1, N+1): <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;for j in range(1, N+1): <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if ( (i + j) == N ) & (i < j): <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count += 1 <br/>
  print(count) <br/>

## The above approach is considered as worst approach. The reason is, the sum pairs that we want is exactly N-1 pairs but the loop is running for N ** 2 times.
## For example, the N is 10, all possible pair is N ** 2(10 ** 2) which is 100 pairs. Out of 100 pairs, the possible sum pair count is 9 which is N-1(10-1).
## Time complexity for this problem is too high which is N**2, running time of the for loop will be N**2.

# 2) Logical Approach:

  From the explanation we've seen that the possible sum pair starts with minimum value of the range given to the variable for A and <br/>
  for B, it starts with N-A. For Example the range given is 1 to N. And the given input N=10. The first pair is (1, N-1) nothing but <br/>
  (1,9). <br/>

  And the second possible is (2,8). If we compared this to the previous input, A is increasing and B is decreasing. That's what we've observed. <br/>
  So, we know that A is increasing and B is decreasing from the example explanation. So, we can go with the looping approach by initializing A and <br/>
  B with appropriate value. Once A is greater than or equal to B we can stop the loop and print the count of pairs of sum. <br/>

  ## PYTHON CODE 
  N, count = int(input()),0 <br/>
  A = 1 <br/>
  B = N - A <br/>
  while A < B: <br/>
      &nbsp;&nbsp;&nbsp;&nbsp;count += 1  <br/>
      &nbsp;&nbsp;&nbsp;&nbsp;A = A + 1  <br/>
      &nbsp;&nbsp;&nbsp;&nbsp;B = N - A  <br/>
  print(count)  <br/>

  From this approach, we've reduce the running time from N**2 to ~ (N - 1) // 2. For example if N=10. The previous running time is (N**2) 100 times. <br/>
  Here, the running time is {(N - 1) // 2} (10-1) // 2 = 9 // 2 = 4. This is a huge difference from 100 times to 4 times. <br/>

# 3) Logical Approach by incorporating Mathematical Knowledge:

  We know that the possible pairs will be N-1 pairs. From N-1 pairs there is no chance of getting possible sum pairs which is greater than N/2 times. 
  It means that half of the pairs will be A < B and Half of the pairs will be A greater than B. In between there is change of getting A == B. A==B will occur only
  when A starts with odd and B starts with odd. In this problem statement A starts with 1 which is odd number and if B value which is N-1 is odd if A is even, there is chance of 
  getting A == B. For example we can see the example explanation 1 where N=10, A==B is available (5,5). <br/>

  For this Problem Statement, we can write condition for even number input. For even number we need the pairs which is above the A==B pair right!!. Then, we  <br/>
  can write formula like this ( (N - 1) - 1) / 2. <br/>

  In the above formula(even), N-1 denotes the number of possible pairs. And again we're reducing 1 that we don't want which is A==B. Then we're dividing the calculated value with 2. <br/>
  For Example N=10, ( (10-1) -1 ) / 2) = ( (9-1) / 2 ) = ( 8 / 2 ) = 4. This is what we want for even numbers. <br/>

  Now, we can look for Odd numbers, <br/>
  For Odd number N values, there is no change of getting A==B. For example N=9. The possible pairs are, <br/>
   (1,8) <br/>
   (2,7) <br/>
   (3,6) <br/>
   (4,5) <br/>
   (5,4) <br/>
   (6,3) <br/>
   (7,2) <br/>
   (8,1) <br/>
  At the same time half of the possible pairs are  A < B pair and another half are A greater than B. For odd N, we can write formula like this, <br/>
  (N - 1) / 2. Eg: N=9, (9-1) / 2 = (8 / 2) = 4. This is what we want for odd numbers. <br/>

  We can write code like this, <br/>
  ## PYTHON CODE 
  N = int(input()) <br/>
  if N & 2 == 0:  <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;print( (N - 2) / 2 ) <br/>
  elif N % 2 != 0: <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;print( (N - 1) / 2) <br/>

# 4) Fine-Tuned Logical Approach by incorporating Mathematical Knowledge

  Here we are reducing 1 or 2 from the N value and the we're diving by 2. This is the common thing in both of the formulas. <br/>
  So, we can write this in single formula. We know that we have to reduce 1 for sure from the N, reason is to get possible pair count. <br/> 
  After reducing 1 from N, then we can go for floor division by 2. It will give only the whole number of the normal division. For Even N value, <br/> 
  the A==B will be not considered.  <br/>
  For Example, N=10, the possible pairs is 9, A==B is possible. If we floor divide by 2, we will get 9 // 2 = 4 and this is what we need.<br/>
  For Example N=9, the possible pairs is 8, A==B not possible. If we floor divide by 2, we will get 8 // 2 = 4 and this is what we need.<br/>

  The Time taken for this approach is 1, means only one caluculation for any input N. Practically less than 1 microsecond (tested in 6 core 12 thread CPU) for any N value. For Eg: <br/>
  N=1000000000000000000000000000000000.<br/>
  If we process this N value in 1st or 2nd, it will take months and months of time to return the output.<br/>

  The Final Best code is, <br/>

  ## PYTHON CODE
  N = int(input()) <br/>
  print( (N - 1) // 2) <br/>
  <br/>
  (or) <br/>
  <br/>
  print( ( int(input()) - 1 ) // 2) <br/>
  

  


   
