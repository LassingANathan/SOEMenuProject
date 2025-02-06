from Category import Category
from FoodItem import FoodItem

class CategoryHolder:    
    def __init__(self, fileString: str, defaultCategoryName="other"):
        # Declare space for categories
        self.categories = []
        self.defaultCategory: Category = None
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
                for i in range(2, len(splitLine)):
                    newFoodItem = FoodItem(0, splitLine[i], newCategory)
                    newCategory.addFoodItem(newFoodItem)
                    
                # Add the created category to Categories
                self.categories.append(newCategory)