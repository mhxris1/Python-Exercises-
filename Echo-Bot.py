
#Echo Bot

counter=0
while True:

    response = input("Enter A Line. To exit type exit, quit or leave empty: \n")
    if response.lower() in ("quit", "exit", ""):
        break
    
    counter += 1
    print(response)
      

print("Program has ended, Goodbye!  \nLines Counter ", counter)