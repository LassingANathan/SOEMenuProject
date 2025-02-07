from SessionController import SessionController

def main(): 
    # Create a list from the following string
    listString = "1 package whole wheat, 2 cups milk, 6 lbs ground beef, 4 cups cheddar cheese, 1 package pizza, 2 oz broccoli, 2 lbs ground beef, 1 cup yogurt, 2 cuts steak"
    
    sessionController = SessionController()
    
    sessionController.addFoodItemToCategory(1, "steak")
    
    print(sessionController.createList(listString))
    
        
main()