# 1) Traditional looping Approach
N, count = int(input()),0
for i in range(1, N+1):
    for j in range(1, N+1):
        if ( (i + j) == N ) & (i < j):
            count += 1
print(count)

# 2) Logical Approach
N, count = int(input()),0
A = 1
B = N - A
while A < B:
    count += 1
    A = A + 1
    B = N - A
print(count)

# 3) Logical Approach by incorporating Mathematical Knowledge
N = int(input())
if N & 2 == 0:
    print( (N - 2) / 2 )
elif N % 2 != 0:
    print( (N - 1) / 2)

# 4) Fine Tuned Logical Approach by incorporating Mathematical Knowledge
print( ( int(input()) - 1 ) // 2)
