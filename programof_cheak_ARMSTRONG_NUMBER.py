def cheak_armstrong_number(num):
    lst = [int(digit)for digit in str(num)]
    sumOfDigits = 0
    for digit in lst:
        sumOfDigits +=digit**3
    if num == sumOfDigits:
        print(num,"is ARMSTRONG NUMBER") 
    else:
        print(num,"is not ARMSTRONG NUMBER")

n = int(input("enter number:"))
cheak_armstrong_number(n)                