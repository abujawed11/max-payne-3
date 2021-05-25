a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

for i in range(a,b+1):
    for x in range(2,i):
        if (i%x)==0:
            break
    else:
        print(i)






