n=int(input())
ar=list(map(int,input().split()))
ar.sort()
for i in range(len(ar)):
    print(ar[i], end=' ')
