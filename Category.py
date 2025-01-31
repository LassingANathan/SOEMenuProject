class Category:
    id: int = None
    name: str = None
    foodItems = []
    
    def __init__(self, id, name):
        self.id = id
        self.name = name