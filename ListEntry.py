class ListEntry:    
    def __init__(self, id, quantity, unitOfMeasurement, itemName):
        self.id: int = id
        self.quantity: float = quantity
        self.unitOfMeasurement: str = unitOfMeasurement
        self.itemName: str = itemName