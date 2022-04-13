m=int(input("m="))
n=int(input("n="))
for i in range(1,m+1):
    for j in range(1,n+1):
        print(format(i*j,'3d'),end=" ")
    print("\n")
