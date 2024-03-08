from bisect import *
t = int(input())
lis = list(map(int,input().split()))
q = int(input())
lis.sort()

for _ in range(q):
    n = int(input())
    print(bisect_right(lis,n))