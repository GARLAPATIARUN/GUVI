# taking user input
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print("Vowel")
if(ch=='$' or ch=='%'):
    print("Invalid")
else:
    print("Consonant")
