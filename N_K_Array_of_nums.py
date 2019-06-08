N=int(input(""))
K=int(input(""))
n=[]
p=0
for i in range(N):
    q = int(input())
    n.append(q)
for p in range(K):
    p=p+n[p]
print(p)
