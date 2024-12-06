print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? please enter S for small, M for medium, L for Large: ")
if size == "L":
    bill = 25
elif size == "M":
    bill = 20
elif size == "S":
    bill = 15
else:
    print("Please enter a valid charater...please enter S for small, M for medium, L for Large:")
pepperoni = input("Do you want pepperoni on your pizza? Y for Yes or N for No")
if pepperoni == "Y":
    if size == "L":
        bill += 3
    elif size == "M":
        bill += 3
    elif size == "S":
        bill += 2
else:
    print("Didnot add extra pepperoni")
extra_cheese = input("Do you want extra cheese? Y or N")
if extra_cheese == "Y":
    bill +=1
else:
    print("Didnot add extra cheese")
print(f"Your total bill is: ${bill}")
