print("Welcome to the roller-coaster!")
height=int(input("Please Enter your height in cm: "))
if height >= 120:
    age = int(input("Please enter your age:"))
    if age <= 18:
        print("Pay $10 for the ticket")
        bill = 10
    elif age <= 12:
        print("Pay $5 for the ticket")
        bill = 5
    elif age >= 45 and age <= 55:
        print("You no need to pay its for free")
        bill = 0
    else:#13 to 17
        print("Pay $7 for the ticket")
        bill = 7
    photo=input("Do you want to take a picture? type Y for yes and N for no")
    if photo == "Y":
        bill +=3
        print(f"Your total bill including photo is: ${bill}")
    else:
        print(f"Your total bill is: ${bill}")
else :
    print("you are not allowed bacause of your height:(")