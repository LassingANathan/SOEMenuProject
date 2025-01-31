class ListEntry:
    id: int = None
    quantity: float = None
    unitOfMeasurement: str = None
    itemName: str = None
    
    def __init__(self, id, quantity, unitOfMeasurement, itemName):
        self.id = id
        self.quantity = quantity
        self.unitOfMeasurement = unitOfMeasurement
        self.itemName = itemName