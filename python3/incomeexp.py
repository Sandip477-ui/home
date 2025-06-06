income = 8000
expense = 5000
balance = income - expense
print(f"income={income}")
print(f"expense={expense}")
print(f"balance is {balance}")

income2 = 10000
expense2 = 5000
print(f"income2 is {income2}\nepxense2 is {expense2}")
print(f"my balance is {income2 - expense2}")



#if income =8000 and expense =5000 whate is the balance ?
income = 8000
expense = 5000
balance = income - expense
print(f"income = {income}")
print(f"expense = {expense}")
print(f"balance is = {balance}")
 
# Q2 if income =10000 and expense = 12000 is there a profit or loss ? How much profit or loss ?
income = 10000
expense = 12000
balance = income - expense
print(f"income = {income}")
print(f"expense = {expense}")
print(f"balance is = {balance}")
# if elif else conditions
if balance >0:
    print("profit amout = {balance}")
elif balance <0:
    print(f"loss amount = {abs(balance)}")
else:  #abs for absolute value function nagitive value changeto positive
    print("no profit no loss")


# take user input for income and expense
income = int(input("enter your income "))
expense = int(input("enter your expense "))
balance = income - expense 
print(f"your balance is {balance}")
# if elif else conditions
if balance >0:
    print(f"profit amount = {balance}")
elif balance <0:
    print(f"loss amount = {abs(balance)}")
else:  #abs for absolute value function nagitive value changeto positive
    print("no profit no loss")

english = int(input("enter your english mark "))
math = int(input("enter your math mark "))
science = int(input("enter your science mark "))
social = int(input("enter your social mark "))

total_mark =english +math+ science+ social 
print(f'your total makrs is {total_mark}')
avg_marke = total_mark/4
print(f"your avrage mark is {avg_marke}")

if avg_marke >90:
    print(f"your gpa is A+ ")
elif avg_marke >80:
    print("your gpa is A")
elif avg_marke >70:
    print(f"your gpa is B+")
else:
    print(f"you are just pass ")
    
    