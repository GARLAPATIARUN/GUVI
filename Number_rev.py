n = int(input())
temp = n
sum=0
while temp!=0:
    digit = temp%10
    sum = (sum*10)+(digit)
    temp=temp//10
print(sum)
