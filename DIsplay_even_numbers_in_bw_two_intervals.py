x,y = map(int, input().split())
a=[]
for i in range(x,y):
    if(i%2==0):
        a.append(i)
print(a)
