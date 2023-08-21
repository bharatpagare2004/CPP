# str = "   bharat"
# str1 = str.replace()
# print(str1)
# print(chr(97))
# print(chr(65))
# print(chr(1200))


# # str = "Hello Python" 
# # for ch in str[ : :-1]:
# #     print(ch)
# import string          
# str = "python is very good scientific programing language"
# print(string.capwords(str))  
from string import Template
t = Template("$name is the $title of the $company")
s = t.substitute(name="Pankaj",title="Founder", company="JournalDev.")
print(s)