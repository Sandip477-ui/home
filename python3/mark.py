#student mark
input("enter your name ")
math=int(input("enter your math mark "))
english=int(input("enter your english mark "))
science=int(input("enter your science mark "))
social=int(input("enter your social mark "))
total= math+english+science+social

avg=total/4
print(f"total mark is {total}")
print(f"average mark is {avg}")


if avg>80:
    print("congratulation your grade is A")
elif avg>60:
    print("congratulation your grade is B")
elif avg>40:
    print("congratulation your grade is C")
else:
    print("congratulation your grade is D")
