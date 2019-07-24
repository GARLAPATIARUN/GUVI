s=str(input())
z=0
for i in range(len(s)):
    if(s[i]=='('):
        z=z+1
    elif(s[i]==')'):
        z=z-1
if(z==0):
    print("yes")
else:
    print("no")
