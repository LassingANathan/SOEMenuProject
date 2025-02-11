from ListCreator import ListCreator
from CategoryHolder import CategoryHolder

class SessionController:
    def __init__(self):
        self.workingCategoriesFileName = "workingCategoryFile.txt"
        self.uneditedCategoriesFileName = "uneditedCategoryFile.txt"
        self.categoryHolder: CategoryHolder = CategoryHolder(self.workingCategoriesFileName)
        self.listCreator = ListCreator(self.categoryHolder)
        
    # Returns a sorted list given the listString
    def createList(self, listString: str):
        return self.listCreator.createListFromString(listString)
    
    # Renames a category in the file and updates the ListCreator
    def renameCategory(self, categoryId: int, newName: str):
        self.categoryHolder.renameCategory(categoryId, newName)
        self.listCreator = ListCreator(self.categoryHolder)
        
    # Removes a given foodItem from the given category and updates the ListCreator
    def removeFoodItemFromCategory(self, categoryId: int, foodItemName: str):
        self.categoryHolder.removeFoodItemFromCategory(categoryId, foodItemName)
        self.listCreator = ListCreator(self.categoryHolder)
        
    def addFoodItemToCategory(self, categoryId: int, foodItemName: str):
        self.categoryHolder.addFoodItemToCategory(categoryId, foodItemName)
        self.listCreator = ListCreator(self.categoryHolder)
        
    def addNewCategory(self, newCategoryName):
        newCategoryId = 0
        # Find the highest id so far
        with open(self.workingCategoriesFileName, "r") as f:
            lines = f.readlines()
            highestIdSoFar = 0
            for line in lines:
                splitLine = line.split("_")
                highestIdSoFar = int(splitLine[0])
                
        newCategoryId = highestIdSoFar + 1
            
        # Append the new category
        with open(self.workingCategoriesFileName, "a") as f:
            f.write(str(newCategoryId) + "_" + newCategoryName)
            
        # Reload category holder and list creator
        self.categoryHolder = CategoryHolder(self.workingCategoriesFileName)
        self.listCreator = ListCreator(self.categoryHolder)
        
    # Save the changes in the working file into the unedited file
    def saveChanges(self):
        lines = None
        
        # Get all lines from the working file
        with open(self.workingCategoriesFileName, "r") as f:
            lines = f.readlines()
            
        # Write the working file to the unedited file
        with open(self.uneditedCategoriesFileName, "w") as f:
            for line in lines:
                f.write(line)
                
        # Reload category holder and list creator
        self.categoryHolder = CategoryHolder(self.workingCategoriesFileName)
        self.listCreator = ListCreator(self.categoryHolder)
        
    # Reset the working category file to match the unedited category file
    def discardChanges(self):
        lines = None
        
        # Get all lines from the uneditedCategoryFile
        with open(self.uneditedCategoriesFileName, "r") as f:
            lines = f.readlines()
            
        # Write the unedited file to the working file
        with open(self.workingCategoriesFileName, "w") as f:
            for line in lines:
                f.write(line)
                
        # Reload category holder and list creator
        self.categoryHolder = CategoryHolder(self.workingCategoriesFileName)
        self.listCreator = ListCreator(self.categoryHolder)
     
    # Return a string explaining the differences between the unedited file and the working file
    def getDifferencesSinceSave(self):
        returnString: str = ""
        uneditedLines = None
        workingLines = None
        
        # Get all lines from the unedited file 
        with open(self.uneditedCategoriesFileName, "r") as f:
            uneditedLines = f.readlines()
            
        # Get all lines from the working file
        with open(self.workingCategoriesFileName, "r") as f:
            workingLines = f.readlines()
            
        # Iterate through all lines 
        for i in range(max(len(uneditedLines), len(workingLines))):
            if i >= len(uneditedLines): # More lines in working, which means we've added categories
                splitWorkingLine = workingLines[i].split("_")
                returnString += ("Added category " + splitWorkingLine[1] + "\n")
                continue
            
            if uneditedLines[i] == workingLines[i]: # Lines match, go to next set of lines
                continue
            else: # Lines do not match
                # Skip if one of the lines is whitespace
                if uneditedLines[i].isspace() or workingLines[i].isspace():
                    continue
                
                # Split lines
                splitWorkingLine = workingLines[i].split("_")
                splitUneditedLine = uneditedLines[i].split("_")
                
                # Check if category is the same
                if splitWorkingLine[0] == splitUneditedLine[0] and splitWorkingLine[1] == splitUneditedLine[1]: # Category is the same
                    # Iterate through items in category
                    for k in range(2, max(len(splitUneditedLine), len(splitWorkingLine))):
                        if splitUneditedLine[k] == splitWorkingLine[k]:
                            continue
                        else:
                            if k+1 < len(splitUneditedLine) and splitWorkingLine[k] == splitUneditedLine[k+1]: # Deleted an item
                                returnString += ("Deleted " + splitUneditedLine[k] + " from category " + splitUneditedLine[1] + "\n")
                                break
                            else: # Added an item
                                returnString += ("Added " + splitWorkingLine[k] + " to category " + splitWorkingLine[1] + "\n")
                                break
        return returnString
                

       
    def getCategories(self):
        return self.categoryHolder.categories