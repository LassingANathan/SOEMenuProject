from SessionController import SessionController

def main(): 
    # Create a list from the following string
    listString = "1 package whole wheat, 2 cups milk, 6 lbs ground beef, 4 cups cheddar cheese, 1 package pizza, 2 oz broccoli, 2 lbs ground beef"
    
    sessionController = SessionController()
    
    print(sessionController.createList(listString))
    
    sessionController.renameCategory(0, "milks")
    
    print(sessionController.createList(listString))
        
main()