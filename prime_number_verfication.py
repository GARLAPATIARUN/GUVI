number=int(input())
if number>1 and number<1000:
    for i in range(2,number):
        if(number%i==0):
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
        
