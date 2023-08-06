print("Find PGCD of Two Numbers")

a=int (input("Input A: "))
b=int (input("Input B: "))
while(a!=b):
    if(a>b):
        a=a-b
    else:
        b=b-a
print('Pgcd of two number is = ',a)