# ----------------------------------------------------------------- #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table'
# ChangeLog: DQualley, Nov. 2 2019, Update steps 2, 3, and 4
#            DQualley, Nov. 5 2019, Update steps 5, 6, and 7
# -------------------------------------------------------------------#

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt" # An object that represents a file
strData = "" # A row of text data from the file
lstRow = () # For extracting data from the file
dicRow = {} # A row of data separated into elements of a dictionary
# {Task,Priority}
lstTable = [] # A dictionary that acts as a 'table' of rows
strMenu = "" # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
objFile = open("ToDoList.txt")
for row in objFile:
    lstRow = row.split(",")
    print(lstRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print() # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open("ToDoList.txt", "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Create the table
        dicRow = {"Task": "Priority"}
        lstTable.append(dicRow)
        strTask = input("Enter a task: ")  # Get user input
        strPriority = input("Enter the priority level: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        strDelTask = input("Which task would you like to delete? ")
        if strDelTask in dicRow:
            del dicRow[strDelTask]
            print("\nOkay, I deleted", strDelTask)
        else:
            print("\nI can't do that!", strDelTask, "doesn't exist in the dictionary.")
        continue
    #Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "a")
        lstTable.append(dicRow)
        objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()
        print("Data saved to file! ")
        continue
    #Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("You are exiting the program! ")
    break  # and Exit the program