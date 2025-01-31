class ListEntry:
    id = None
    quantity = None
    unitOfMeasurement = None
    itemName = None
    
    def __init__(self, id, quantity, unitOfMeasurement, itemName):
        self.id = id
        self.quantity = quantity
        self.unitOfMeasurement = unitOfMeasurement
        self.itemName = itemName