"""Student Id = 20CE063
Student name = Preet Padariya"""
#You are given a string and your task is to swap cases.
#In other words, convert all lowercase letters to uppercase letters and vice versa.
def swapcase(Str):
x = ""
for i in Str:
if i.isupper() == True: 
x += (i.lower())
else:
x += (i.upper()) 
return x
if __name__ == '__main__':
Str = input() 
Answer = swapcase(Str)
print(Answer) 
