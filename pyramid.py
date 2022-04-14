#code for building steps in super mario game from pset1 of cs50

#promt for input from user
x=int(input("enter a number: "))
y=x
n=x

#constructing a square loop

for i in range(x):
    for j in range(y):
        if (i+1)<n:
            print(" ", end="")
            i=i+1
        else:
            print("#", end="")
    print("")
