x = 6

for i in range(1, x+1):
    for j in range(1, x-i+1):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end="")
    print()
             
