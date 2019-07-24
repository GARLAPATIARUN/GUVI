def fact(x):
    result = 1
    for i in range(2,x+1):
        result = result*i
    return result
x=int(input())
y=fact(x)
print(y)
