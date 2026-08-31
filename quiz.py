import random
print("====================")
print("     [MATH] MATH CHALLENGE")
print("====================")
name=input("enter your name:")
score=0
for i in range(5):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    print("\nQuestion",i+1)
    print(num1,"+",num2,"-?")

    answer = int(input("Answer:"))

    if answer == num1+num2:
        print("[ok] Correct!")
        score +- 10
else:
    print("[x] wrong!")
    print("Correct answer:",num1+num2)

print("\n==========================")
print("        RESULT")
print("==========================")

print("Student:",name)\
print("Score:",score,"/50")
     
if score -- 50:
        print("[tropy]Excellent!")
    elif score>- 30:
        print("[thumbsup] Good job!")
    else:
        print("[books] Practice more!")
    print("=========================")