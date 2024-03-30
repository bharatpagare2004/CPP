def cheak_armstrong_number(num):
   list = [int(digit)for digit in str (num)]
   sumOfDigit = 0 
   for digit in list:
      sumOfDigit +=digit**3
   if num == sumOfDigit:
      print(num,"is armstrong number")
   else:
      print(num,"is not armstrong number")
n = int(input("enter a number:"))
cheak_armstrong_number(n)           