from ListEntry import ListEntry
from Category import Category

class List:    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.listEntries = [] # Holds ListEntry objects
        self.categoryToListEntryDict = {} # Holds pairs of Category objects to arrays of ListEntries
        
    def addListEntryToList(self, listEntry: ListEntry):
        self.listEntries.append(listEntry)
        
    def __str__(self):
        returnString = ""
        # Iterate through categories
        for category in self.categoryToListEntryDict:
            # Print category name in uppercase
            returnString += category.name.upper().strip() + ":\n"
            # Iterate through ListEntries in current category
            for item in self.categoryToListEntryDict[category]:
                # Print quantity, unit, and item name of the current item
                returnString += str(item.quantity) + " "
                returnString += item.unitOfMeasurement.title() + " "
                returnString += item.itemName.title() + "\n"
        return returnString