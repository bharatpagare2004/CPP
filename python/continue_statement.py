#sample program on continue statement.
x=0
while x<10 :
    x+=1
    if x>5:
        continue
    print("x= ",x)
print("out of loop")