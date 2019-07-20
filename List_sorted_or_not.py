n=int(input())
ar=list(map(int,input().split()))
br=ar[:]
br.sort()
if(ar==br):
    print("yes")
else:
    print("no")
