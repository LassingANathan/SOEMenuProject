from ListCreator import ListCreator
from CategoryHolder import CategoryHolder

class SessionController:
    def __init__(self):
        self.categoryHolder: CategoryHolder = CategoryHolder("defaultCategories.txt")
        self.listCreator = ListCreator(self.categoryHolder)
        
    # Returns a sorted list given the listString
    def createList(self, listString: str):
        return self.listCreator.createListFromString(listString)
    
    # Renames a category in the file and updates the ListCreator
    def renameCategory(self, categoryId: int, newName: str):
        self.categoryHolder.renameCategory(categoryId, newName)
        self.listCreator = ListCreator(self.categoryHolder)