from Category import Category
from FoodItem import FoodItem
from ListCreator import ListCreator
from List import List

def main():
    categories = []
    defaultCategory: Category = None # The category to sort unknown items into
    # Load categories
    with open('defaultCategories.txt', 'r') as categoryFile:
        # Iterate through file
        for line in categoryFile:
            splitLine = line.split("_")
            # Create new category
            newCategory: Category = Category(0, splitLine[0])
            if newCategory.name == "other":
                defaultCategory = newCategory
            
            # Get and add all items in the current category
            for i in range(1, len(splitLine)):
                newFoodItem = FoodItem(0, splitLine[i], newCategory)
                newCategory.addFoodItem(newFoodItem)
                
            # Add the created category to Categories
            categories.append(newCategory)
    
    # Create a list from the following string
    listString = "1 package whole wheat, 2 cups milk, 6 lbs ground beef, 4 cups cheddar cheese, 1 package pizza, 2 oz broccoli, 2 lbs ground beef"
    listCreator = ListCreator(categories, defaultCategory)
    newList : List = listCreator.createListFromString(listString)
    
    print(newList)
        
main()