import Category

class FoodItem:
    def __init__(self, id, name, category: Category):
        self.id = id
        self.name = name
        self.category = category