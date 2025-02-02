from Category import Category
from FoodItem import FoodItem

def main():
    categories = []
    # Load categories
    with open('defaultCategories.txt', 'r') as categoryFile:
        # Iterate through file
        for line in categoryFile:
            splitLine = line.split("_")
            # Create new category
            newCategory: Category = Category(0, splitLine[0])
            
            # Get and add all items in the current category
            for i in range(1, len(splitLine)):
                newFoodItem = FoodItem(0, splitLine[i], newCategory)
                newCategory.addFoodItem(newFoodItem)
                
            # Add the created category to Categories
            categories.append(newCategory)
                
    print(categories)
        
main()