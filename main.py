from SessionController import SessionController
import zmq
import os

context = zmq.Context()
RECIPE_SOCKET_PORT = "tcp://localhost:5555"
ESTIMATOR_SOCKET_PORT = "tcp://localhost:5556"
IDEA_SOCKET_PORT = "tcp://localhost:5557"
SCRAPER_SOCKET_PORT = "tcp://localhost:5558"

# Create socket for recipe microservice
recipeSocket = context.socket(zmq.REQ)
recipeSocket.connect(RECIPE_SOCKET_PORT)

# Create socket for estimator microservice
estimatorSocket = context.socket(zmq.REQ)
estimatorSocket.connect(ESTIMATOR_SOCKET_PORT)

# Create socket for scraper microservice
scraperSocket = context.socket(zmq.REQ)
scraperSocket.connect(SCRAPER_SOCKET_PORT)

sessionController = SessionController()

def mainMenu(): 
    while True:
        # Display options
        print("1: Create List\n2: Category Settings\n3: Recipes\n4: Quit")
        userInput = input()
        
        if userInput == "1":
            listCreationMenu()
        elif userInput == "2":
            settingsMenu()
        elif userInput == "3":
            recipesMenu()
        elif userInput == "4":
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
        print("Enter a list of groceries, separated by line or commas, enter T for a Tutorial, enter R to add ingredients from an online recipe, or enter B to go Back")
        userInput = input()
        
        if userInput == "T":
            print("~~~~~~")
            print("Enter a list of food items, separated either by line or by commas (or both!), and we'll automatically sort it for you.")
            print("Specify a quantity by entering a number and unit before the product name (e.g., \"1 box eggs\", \"2/3 cup milk\")")
            print("Hit enter to submit your list and have it be sorted")
            print("~~~~~~")
        elif userInput == "R":
            # Prompt for file path
            recipeFilePath = input("Enter the filepath of an HTML file from 'SimplyRecipes': ")
            
            # Request and recieve ingredients
            scraperSocket.send_string(os.getcwd() + "\\" + recipeFilePath)
            ingredientsAsString = scraperSocket.recv_string()
            
            # Add the ingredients to the enteredList and continue
            sortedListResponse = sortedListMenu(enteredList, sessionController.createList(ingredientsAsString))
            if sortedListResponse == "1":
                editingList = True
                continue
            return
        elif userInput == "B":
            return
        else:
            enteredList = userInput
            sortedListResponse = sortedListMenu(enteredList, sessionController.createList(userInput))
            if sortedListResponse == "1":
                editingList = True
                continue
            return
            
# Menu for displaying the sorted list,
#param:enteredString=the actual string that was entered by the user
#param:sortedList=the sorted List object created from the enteredString
#return: None if nothing more needs to be done, and 1 if more items need to be added
def sortedListMenu(enteredString: str, sortedList) -> int:
    global estimatorSocket
    
    # Display list
    print("Here's your sorted list:")
    print(sortedList)
    print("~~~~~~")
    
    # Get and display estimated cost
    estimatorSocket.send_string(str(sortedList))
    print("Estimated cost: $" + estimatorSocket.recv_string())
    
    while True:
        # Display options
        print("1: Enter More Items\n2: Edit Categories\n3: Main Menu")
        userInput = input()
        
        if userInput == "1":
            return 1
        elif userInput == "2":
            settingsMenu()
            sortedList = sessionController.createList(enteredString)
            print("Here's your sorted list:")
            print(sortedList)
            print("~~~~~~")
            continue
        elif userInput == "3":
            return
        else:
            continue

def settingsMenu():
    # Get input for Categories
    while True:
        # Get the categories
        categories = sessionController.getCategories()
        print("CATEGORIES:")
        
        # Print all categories
        for i in range(len(categories)):
            print(str(i) + ": " + categories[i].name.title().strip())
        # Prompt
        print("Enter the number before a category to edit that category, enter \"N\" to create a new category, enter \"S\" to save your changes, or enter \"B\" to leave WITHOUT saving your changes")
        userInput = input()
        
        if userInput == "N": # Create new category
            newCategoryName = input("Enter the name of the new category: ")
            sessionController.addNewCategory(newCategoryName.lower())
            continue
        elif userInput == "S": # Save changes
            print("Are you sure you want to save the changes? You've changed the following:")
            print(sessionController.getDifferencesSinceSave())
            print("Are you sure you want to save these changes? This CANNOT be undone.")
            confirmation = input("Enter Y for Yes, and N for No:")
            
            if confirmation == "Y":
                sessionController.saveChanges()
                return
            else:
                continue
        elif userInput == "B": # Leave, don't save
            sessionController.discardChanges()
            return
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
                    print("You've changed the following:")
                    print(sessionController.getDifferencesSinceSave())
                    print("Are you sure you want to save these changes? This CANNOT be undone.")
                    confirmation = input("Enter Y for Yes, and N for No:")
                    
                    if confirmation == "Y":
                        sessionController.saveChanges()
                        return
                    else:
                        continue
                elif userInput == "B": # Leave, don't save
                    sessionController.discardChanges()
                    break
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

def recipesMenu():
    global recipeSocket
    while True:
        # Display options
        print("1: Add Recipe\n2: Retrieve Recipe\n3: Quit")
        userInput = input()
        
        if userInput == "1":
            newRecipeName = input("Enter the name of the new recipe: ")
            newRecipeIngredients = input("Enter a comma separated list of the ingredients: ")
            
            # Get ingredients as a list
            newRecipeIngredients = newRecipeIngredients.split(",")
            for i in range(len(newRecipeIngredients)):
                newRecipeIngredients[i] = newRecipeIngredients[i].strip()
                   
            saveRequest = {
                "command": "save",
                "name": newRecipeName,
                "ingredients": newRecipeIngredients
            }
            
            recipeSocket.send_json(saveRequest)
            print(recipeSocket.recv_json())
        elif userInput == "2":
            # Get recipe name
            requestedRecipeName = input("Enter the name of the recipe to retrieve: ")
            
            # Request recipe
            getRequest = {"command": "get", "name": requestedRecipeName}
            recipeSocket.send_json(getRequest)
            
            # Recieve and display recipe
            recipeResponse = recipeSocket.recv_json()
            print(requestedRecipeName + " Recipe:\n" + recipeResponse)
        elif userInput == "3":
            return
        else:
            continue
    
        
mainMenu()