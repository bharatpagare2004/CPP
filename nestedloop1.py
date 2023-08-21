# for r in range(1,15):
#   for c in range(1,r+1):
#     print("*",end="")
#   print()




# for r in range(1,12):
#     for c in range(1, r+1):
#         print("&",end="")

lst=[67,78,4,7,9,9,0,67,56]
print("enter element to search:")
search=int(input())
for element in lst :
    if search ==element:
        print("element found in list")
        break 
else:
    print("element not found in list")
