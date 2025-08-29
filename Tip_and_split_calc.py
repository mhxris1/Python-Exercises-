while True:
    bill = input("What is your total Bill \n")
    bill_check = bill.isdigit()
    if bill_check==False:
        print("Please Enter Numbers only \n")
        continue
    else:
        break
    

while True:
    tip= input("What percentage tip would you like to give \n")
    if "%" in tip:
        tip=tip.replace("%","")
        tip_check = tip.isdigit()
        if tip_check == True:
            break
        else:
            print("Please Enter Numbers only \n")
    else:
        break

while True:
    split=input("How many people are splitting the bill \n")
    split_check = split.isdigit()
    if split_check==False:
        print("Please Enter Numbers only \n")
        continue
    else:
        break


tip_amount = float(bill)*float(tip)/100
total_amount=float(tip_amount)+float(bill)
share_amount=float(total_amount)/float(split)

print(f"You're tipping ${tip_amount:.2f}")
print(f"Your total amount is ${total_amount:.2f}")
print(f"Each of you owe ${share_amount:.2f}")

