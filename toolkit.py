def add_two_numbers(a,b):
    return a+b
def is_even(number):
    return a+b
def reverse_string(text):
    return a+b
def menu():
    print("========SIMPLE FUNCTION TOOLKIT========")
    print("1.add two numbers")
    print("2.check even or odd")
    print("3.Reverse a string")
    print("4.Exit")
    choice=input("Enter your choice(1-4):")
    if choice =="1":
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print(f"Sum={add_two_numbers(a,b)}")
        
    elif choice=="2":
        num=int(input("Enter a number"))
        print(f"is even:{is_even(num)}")
        
    elif choice=="3":
        text=input("Enter a word or sentence:")
        print(f"Reversed:{reverse_string(text)}")
        
    elif choice=="4":
        print("Goodbye!")
        return
    else:
        print("invalid choice,try agin.")
    menu()
    
if__name__=="__main__":
    menu()
