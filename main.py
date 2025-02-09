from SessionController import SessionController
from List import List

sessionController = SessionController()

def mainMenu(): 
    while True:
        # Display options
        print("1: Create List\n2: Settings\n3: Quit")
        userInput = input()
        
        if userInput == "1":
            listCreationMenu()
        elif userInput == "2":
            settingsMenu()
        elif userInput == "3":
            return
        else:
            continue
        
def listCreationMenu():
    editingList = False
    userInput = ""
    enteredList = ""
    while True:
        if editingList:
            print("Here's your previously entered list:")
            print(enteredList)
            print("~~~~~~")
            
        # Display options
        print("Enter a list of groceries, separated by line or commas,\n or enter T for a Tutorial")
        userInput = input()
        
        if userInput == "T":
            print("~~~~~~")
            print("Enter a list of food items, separated either by line or by commas (or both!), and we'll automatically sort it for you.")
            print("Specify a quantity by entering a number and unit before the product name (e.g., \"1 box eggs\", \"2/3 cup milk\")")
            print("Hit enter to submit your list and have it be sorted")
            print("~~~~~~")
        else:
            enteredList = userInput
            sortedListResponse = sortedListMenu(userInput, sessionController.createList(userInput))
            if sortedListResponse == "1":
                editingList = True
                continue
            return
            
# Menu for displaying the sorted list,
#param:enteredString=the actual string that was entered by the user
#param:sortedList=the sorted List object created from the enteredString
#return: None if nothing more needs to be done, and 1 if more items need to be added
def sortedListMenu(enteredString: str, sortedList: List) -> int:
    print("Here's your sorted list:")
    print(sortedList)
    print("~~~~~~")
    while True:
        # Display options
        print("1: Enter More Items\n2: Edit Categories\n3: Main Menu")
        userInput = input()
        
        if userInput == "1":
            return 1
        elif userInput == "2":
            settingsMenu()
        elif userInput == "3":
            return
        else:
            continue

def settingsMenu():
    pass

def categorySettingMenu():
    pass
    
        
mainMenu()