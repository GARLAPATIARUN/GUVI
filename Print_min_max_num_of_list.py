N=int(input())
ar=list(map(int,input().split()))
ar.sort()
print(min(ar),max(ar),end=' ')
