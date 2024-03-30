print("bharat")


#basic pay program
basicpay=int(input("enter basic pay:"))
hra=basicpay*0.1
ta=basicpay*0.05
grosssal=basicpay+hra+ta
proftax=grosssal*0.02
netsal=grosssal-proftax
print("salary payable is ,net salary ")
