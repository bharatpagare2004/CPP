# left triange pattern
n = int(input("enter a  number:"))
for i in range(n+2):
    for j in range (1, i+1):
        print(j, end= "")
    print()    