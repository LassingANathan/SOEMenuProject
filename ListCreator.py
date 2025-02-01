import Category, FoodItem, List, ListEntry
import re

class ListCreator:
    #@param:Categories is a dictionary of category names to food names, to be used for list sorting
    def __init__(categories: map):
        pass
    
    # Creates and returns a list from a string
    def createListFromString(self, string: str) -> List:
        newList: List = List(0, "New List!!!")
        
        # Get all entries from the strings into a list
        stringEntries = re.split(', |\\n ', string)
        # Remove all trailing/leading whitespace
        for i in range(len(stringEntries)):
            stringEntries[i] = stringEntries[i].strip()
        
        # Iterate through stringEntries, creating ListEntries for each line
        for i in range(len(stringEntries)):
            currentLineAsList = stringEntries[i].split()
            
            currentEntryQuantity: float = float(currentLineAsList[0])
            currentEntryUnit: str = currentLineAsList[1]
            # Turn the remainder of the list into a single string with spaces separating them
            currentEntryName: str = " ".join(str(x) for x in currentLineAsList[2:])
            
            # Create the new ListEntry and add it to the List
            newListEntry: ListEntry = ListEntry(i - 1, currentEntryQuantity, currentEntryUnit, currentEntryName)
            newList.addEntryToList(newListEntry)
