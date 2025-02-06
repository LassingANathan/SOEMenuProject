from Category import Category
from FoodItem import FoodItem

class CategoryHolder:    
    def __init__(self, fileString: str, defaultCategoryName="other"):
        self.categoriesFileString = fileString
        
        # Declare space for categories
        self.categories = []
        self.defaultCategory: Category = None
        self.loadCategories(self.categoriesFileString, defaultCategoryName)
                
    # Load all categories into a list
    def loadCategories(self, fileString: str, defaultCategoryName: str):
        # Load categories
        with open(fileString, 'r') as categoryFile:
            # Iterate through file
            for line in categoryFile:
                splitLine = line.split("_")
                # Create new category
                newCategory: Category = Category(splitLine[0], splitLine[1])
                if newCategory.name == defaultCategoryName:
                    self.defaultCategory = newCategory
                
                # Get and add all items in the current category
                ##TODO At some point, we'll want to add IDs to every food item
                for i in range(2, len(splitLine)):
                    newFoodItem = FoodItem(0, splitLine[i], newCategory)
                    newCategory.addFoodItem(newFoodItem)
                    
                # Add the created category to Categories
                self.categories.append(newCategory)
            
    # Renames a category with the given ID to the newName    
    def renameCategory(self, categoryId: int, newName: str):
        pass
    
    # Removes a foodItem from the given category
    def removeFoodItemFromCategory(self, categoryId: int, foodItemName: str):
        pass
    
    # Adds a new foodItem with the given name to the given category
    def addFoodItemToCategory(self, categoryId: int, foodItemName: str):
        pass