while True:
    try:
        number = int(input("Height: "))
        if 1<=number<=8:
            break
    except:
        number=input("Height: ")

for i in range(1,number+1):
    print(" "*(number-i),end="")
    print("#"*i,end="")
    print(" "*2,end="")
    print("#"*i)

