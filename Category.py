import FoodItem

class Category:    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.foodItems = []
        
    def addFoodItem(self, foodItem: FoodItem):
        self.foodItems.append(foodItem)