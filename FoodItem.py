import Category

class FoodItem:
    id: int = None
    name: str = None
    category: Category = None
    
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category