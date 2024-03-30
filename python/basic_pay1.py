basic_pay = int(("enter your basic pay:"))
hra = basic_pay*0.1
ta=basic_pay*0.05
gross_sal = basic_pay +hra +ta
prof_tax =gross_sal*0.02
net_sal =gross_sal-prof_tax
print("salary payable is ",net_sal)