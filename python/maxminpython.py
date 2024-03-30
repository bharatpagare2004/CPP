n=int(input("enter how many nos of element in list:"))
lst=[]
for i in range(n):
    num=int(input("enter element:"))
    lst.append(num)
maxno=max(lst)
minno=min(lst)
sumno=sum(lst)
average=sumno/len(lst)
print("max no :",maxno)
print("min no :",minno)
print("count of lst element:",len(lst))
print("sum of all element:",sumno)
print("average of all element",average)