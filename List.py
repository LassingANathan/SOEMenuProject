import ListEntry

class List:    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.listEntries = []
        
    def addListEntryToList(self, listEntry: ListEntry):
        self.listEntries.append(listEntry)