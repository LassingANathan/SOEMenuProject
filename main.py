from Category import Category
from FoodItem import FoodItem
from ListCreator import ListCreator
from List import List
from CategoryHolder import CategoryHolder

def main():
    categoryHolder: CategoryHolder = CategoryHolder("defaultCategories.txt")
    
    # Create a list from the following string
    listString = "1 package whole wheat, 2 cups milk, 6 lbs ground beef, 4 cups cheddar cheese, 1 package pizza, 2 oz broccoli, 2 lbs ground beef"
    listCreator = ListCreator(categoryHolder)
    newList : List = listCreator.createListFromString(listString)
    
    print(newList)
        
main()