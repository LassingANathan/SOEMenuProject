from List import List
from ListEntry import ListEntry
from Category import Category
from CategoryHolder import CategoryHolder
from word2number import w2n
import re

class ListCreator:
    #@param:Categories is a list of Category objects
    def __init__(self, categoryHolder: CategoryHolder):
        self.categoryHolder: CategoryHolder = categoryHolder
        self.categories: list = self.categoryHolder.categories
        self.defaultCategory: Category = self.categoryHolder.defaultCategory

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
            if currentLineAsList[0].isnumeric():
                currentEntryQuantity: float = float(currentLineAsList[0])
            else:
                currentEntryQuantity: float = float(w2n.word_to_num(currentLineAsList[0]))
            currentEntryUnit: str = currentLineAsList[1]
            
            # Turn the remainder of the list (the item name) into a single string with spaces separating them
            currentEntryName: str = " ".join(str(x) for x in currentLineAsList[2:])
            
            # Check if a previously created list entry has the same units and name
            isNewItem: bool = True
            for listEntry in newList.listEntries:
                # If entries match, then edit the original entry
                if listEntry.itemName.lower() == currentEntryName.lower() and listEntry.unitOfMeasurement.lower() == currentEntryUnit:
                    listEntry.quantity += currentEntryQuantity
                    isNewItem = False
                    break
                
            # Don't add the new entry to the List if the item isn't new, since we already just updated the old entry
            if not isNewItem:
                continue
            
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
                        currentItemCategory = category
            
            # Add the item to the list's dict, creating a new pair or appending as necessary
            try:
                newList.categoryToListEntryDict[currentItemCategory].append(newListEntry)
            except KeyError:
                newList.categoryToListEntryDict[currentItemCategory] = [newListEntry]
                
        return newList
