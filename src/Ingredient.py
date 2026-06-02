class Ingredient:
    def __init__(self, name:str,quantity:float,unit:str):
        self.name=name
        self.quantity=quantity
        self.unit=unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        num=float(value)
        if num<=0:
            raise ValueError("Кол-во должно быть положительным")
        self._quantity=num

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingridient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other,Ingredient):
            return NotImplemented
        return self.name==other.name and self.unit==other.unit