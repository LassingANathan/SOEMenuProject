from Category import Category
from FoodItem import FoodItem

class CategoryHolder:    
    def __init__(self, fileString: str, defaultCategoryName="other"):
        self.categoriesFileString = fileString
        self.defaultCategoryName = defaultCategoryName
        
        # Declare space for categories
        self.categories = []
        self.defaultCategory: Category = None
        self.loadCategories(self.categoriesFileString, defaultCategoryName)
                
    # Load all categories into a list
    def loadCategories(self, fileString: str, defaultCategoryName: str):
        # Reset any current categories
        self.categories = []
        
        # Load categories
        with open(fileString, 'r') as categoryFile:
            # Iterate through file
            for line in categoryFile:
                splitLine = line.split("_")
                # Create new category
                newCategory: Category = Category(splitLine[0], splitLine[1])
                if newCategory.name.lower().strip() == defaultCategoryName:
                    self.defaultCategory = newCategory
                
                # Get and add all items in the current category
                ##TODO At some point, we'll want to add IDs to every food item
                for i in range(2, len(splitLine)):
                    newFoodItem = FoodItem(0, splitLine[i].strip(), newCategory)
                    newCategory.addFoodItem(newFoodItem)
                    
                # Add the created category to Categories
                self.categories.append(newCategory)
            
    # Renames a category with the given ID to the newName    
    def renameCategory(self, categoryId: int, newName: str):
        lines = None
        
        # Get all lines from the category file
        with open(self.categoriesFileString, "r") as f:
            lines = f.readlines()
            
        # Write back all content, except change the name of the category
        with open(self.categoriesFileString, "w") as f:
            for line in lines:
                # Split the line
                splitLine = line.split("_")
                if splitLine[0] != str(categoryId): # Not the category to edit
                    f.write(line.lower())
                else: # Category to edit
                    # Update the category's name
                    splitLine[1] = newName
                    # Rejoin the line into a string and write it
                    lineToWrite = "_".join(str(i) for i in splitLine)
                    f.write(lineToWrite.lower())
                    
        # Reload categories now that the file is corrected
        self.loadCategories(self.categoriesFileString, self.defaultCategoryName)         
    # Removes a foodItem from the given category
    def removeFoodItemFromCategory(self, categoryId: int, foodItemName: str):
        lines = None
        
        # Get all lines from the category file
        with open(self.categoriesFileString, "r") as f:
            lines = f.readlines()
            
        # Write back all content, except without the foodItem
        with open(self.categoriesFileString, "w") as f:
            for line in lines:
                # Split the line
                splitLine = line.split("_")
                # Strip all words in line
                for i in range(len(splitLine)):
                    splitLine[i] = splitLine[i].strip()

                if splitLine[0] != str(categoryId): # Not the category to edit
                    f.write(line.lower().strip() + "\n")
                else: # Category to edit
                    # Remove the food item from the split line
                    splitLine.remove(foodItemName.lower().strip())
                    # Rejoin the line into a string and write it
                    lineToWrite = "_".join(str(i) for i in splitLine)
                    f.write(lineToWrite.lower().strip() + "\n")
                    
        # Reload categories now that the file is corrected
        self.loadCategories(self.categoriesFileString, self.defaultCategoryName)
    
    # Adds a new foodItem with the given name to the given category
    def addFoodItemToCategory(self, categoryId: int, foodItemName: str):
        lines = None
        
        # Get all lines from the category file
        with open(self.categoriesFileString, "r") as f:
            lines = f.readlines()
            
        # Write back all content, except now with the new foodItem
        with open(self.categoriesFileString, "w") as f:
            for line in lines:
                # Split the line
                splitLine = line.split("_")
                # Strip all words in line
                for i in range(len(splitLine)):
                    splitLine[i] = splitLine[i].strip()

                if splitLine[0] != str(categoryId): # Not the category to edit
                    f.write(line.lower().strip() + "\n")
                else: # Category to edit
                    # Add the new item to the split line
                    splitLine.append(foodItemName.lower().strip())
                    # Rejoin the line into a string and write it
                    lineToWrite = "_".join(str(i) for i in splitLine)
                    f.write(lineToWrite.lower().strip() + "\n")
                    
        # Reload categories now that the file is corrected
        self.loadCategories(self.categoriesFileString, self.defaultCategoryName)