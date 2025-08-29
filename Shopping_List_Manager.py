print("Shopping List: \n")
print("Commands \n \n Add [x] - adds item \n Remove [x] - removes item \n Show - Shows list \n Clear - Clears list \n Quit - Ends program \n")
shopping_list=[]
program = True

while program==True:
    command=input("Type in your command: \n").lower()
    if "add" in command:
        new_command=command.replace("add","").strip()
        shopping_list.append(new_command)
    elif "remove" in command:
        new_command=command.replace("remove","").strip()
        if new_command in shopping_list:
                 shopping_list.remove(new_command)
        else:
            print("This item doesn't exist. Please try again \n")
    elif "show" in command:
        for i in shopping_list:
            print(f"\n -{i}\n")
    elif "clear" in command:
        shopping_list.clear()
    elif "quit" in command:
        program=False
    else:
        print("Incorrect Input. Please try again")

print("\nHere is your shopping list:\n")
for i in shopping_list:
    print(f" - {i} \n")

# This program was built with the intention of applying the skills and knowledge of List Handling in Python.
# It utilises the basic loops in python and is an interactive piece of code.

    
