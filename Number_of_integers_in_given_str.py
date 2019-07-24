p=str(input())
b=len(p)
c=0
for i in range(b):
    if(p[i].isdigit()==True):
        c=c+1
print(c)
