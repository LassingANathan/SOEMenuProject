from List import List
from ListEntry import ListEntry
from Category import Category
import re

class ListCreator:
    #@param:Categories is a list of Category objects
    def __init__(self, categories: list, defaultCategory: Category):
        self.categories = categories
        self.defaultCategory = defaultCategory
    
    # Creates and returns a list from a string
    def createListFromString(self, string: str) -> List:
        newList: List = List(0, "New List!!!")
        
        # Get all entries from the strings into a list
        stringEntries = re.split(', |\\n ', string)
        # Remove all trailing/leading whitespace
        for i in range(len(stringEntries)):
            stringEntries[i] = stringEntries[i].strip()
        
        # Iterate through stringEntries, creating ListEntries for each line and adding them to the List's dict
        for i in range(len(stringEntries)):
            currentLineAsList = stringEntries[i].split()
            
            # Get quantity and units for current item
            currentEntryQuantity: float = float(currentLineAsList[0])
            currentEntryUnit: str = currentLineAsList[1]
            
            # Turn the remainder of the list (the item name) into a single string with spaces separating them
            currentEntryName: str = " ".join(str(x) for x in currentLineAsList[2:])
            
            # Create the new ListEntry and add it to the List
            newListEntry: ListEntry = ListEntry(i - 1, currentEntryQuantity, currentEntryUnit, currentEntryName)
            newList.addListEntryToList(newListEntry)
            
            ## Find which category this item belongs to
            currentItemCategory = self.defaultCategory
            # Iterate through Categories
            for category in self.categories:
                # Iterate through the FoodItems in the current Category
                for foodItem in category.foodItems:
                    if foodItem.name == newListEntry.itemName:
                        currentItemCategory = category.name
            
            # Add the item to the list's dict, creating a new pair or appending as necessary
            try:
                newList.categoryToListEntryDict[currentItemCategory].append(newListEntry)
            except KeyError:
                newList.categoryToListEntryDict[currentItemCategory] = [newListEntry]
                
        return newList
