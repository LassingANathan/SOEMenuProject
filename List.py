import ListEntry

class List:
    id: int = None
    name: str = None
    listEntries = []
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def addListEntryToList(self, listEntry: ListEntry):
        self.listEntries.append(listEntry)