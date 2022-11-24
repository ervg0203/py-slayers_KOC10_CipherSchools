a=int(input("Enter number here:"))
for b in range(2,a+1):
    print("Table of",b,":")
    for i in range(1,11):
        print(b,"x",i,"=",b*i)
    print()
