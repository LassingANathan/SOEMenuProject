from SessionController import SessionController
from List import List
from Category import Category

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
            sortedListResponse = sortedListMenu(sessionController.createList(userInput))
            if sortedListResponse == "1":
                editingList = True
                continue
            return
            
# Menu for displaying the sorted list,
#param:enteredString=the actual string that was entered by the user
#param:sortedList=the sorted List object created from the enteredString
#return: None if nothing more needs to be done, and 1 if more items need to be added
def sortedListMenu(sortedList: List) -> int:
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
    # Get input for Categories
    while True:
        # Get the categories
        categories = sessionController.getCategories()
        
        # Print all categories
        for i in range(len(categories)):
            print(str(i) + ": " + categories[i].name.title())
        # Prompt
        print("Enter the number before a category to edit that category, enter \"N\" to create a new category, enter \"S\" to save your changes, or enter \"B\" to leave WITHOUT saving your changes")
        userInput = input()
        
        if userInput == "N": # Create new category
            newCategoryName = input("Enter the name of the new category: ")
            sessionController.addNewCategory(newCategoryName.lower())
            continue
        elif userInput == "S": # Save changes
            pass
        elif userInput == "B": # Leave, don't save
            break
        elif userInput.isdigit() and int(userInput) < len(categories): # Edit category 
            categoryChoice = userInput
            categories = sessionController.getCategories()
            currentCategory = categories[int(categoryChoice)]   
            currentCategoryItems: list = currentCategory.foodItems    
            # Get input for FoodItems
            while True:  
                # Print all foodItems
                for i in range(len(currentCategoryItems)):
                    print(str(i) + ": " + currentCategoryItems[i].name.title())
                # Prompt
                print("Enter the number before an item to DELETE that item, enter \"N\" to create a new item, or enter \"S\" to save your changes, or enter \"B\" to leave WITHOUT saving your changes")
                userInput = input()
                
                if userInput == "N": # Create new FoodItem
                    newFoodItemName = input("Enter the name of the new item: ")
                    sessionController.addFoodItemToCategory(currentCategory.id, newFoodItemName)
                    # Reload categories after change was made
                    categories = sessionController.getCategories()
                    currentCategory = categories[int(categoryChoice)]             
                    currentCategoryItems: list = currentCategory.foodItems
                    continue
                elif userInput == "S": # Save changes
                    pass
                elif userInput == "B": # Leave, don't save
                    return
                elif userInput.isdigit() and int(userInput) < len(currentCategoryItems): # DELETE a FoodItem
                    sessionController.removeFoodItemFromCategory(currentCategory.id, currentCategoryItems[int(userInput)].name)
                    # Reload categories after change was made
                    categories = sessionController.getCategories()
                    currentCategory = categories[int(categoryChoice)]             
                    currentCategoryItems: list = currentCategory.foodItems
                    continue
                else:
                    pass
        else: # Not recognized input
            continue

def categorySettingMenu():
    pass
    
        
mainMenu()