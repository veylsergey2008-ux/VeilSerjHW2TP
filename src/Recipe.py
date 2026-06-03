from Ingredient import Ingredient
class Recipe:
    def __init__(self, title:str,ingredients=None):
        self.title=title
        self.ingredients=ingredients.copy() if ingredients else []

    def add_ingredient(self,ingredient:"Ingredient"):
        for existIngredient in self.ingredients:
            if existIngredient==ingredient:
                existIngredient.quantity+= ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio,(int,float)) and ratio>0:
            return True
        else:
            return False

    def scale(self,ratio:float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэф множителя должен быть больше нуля")
        scaleIngredients=[]
        for i in self.ingredients:
            scaleI=Ingredient(i.name,i.quantity*ratio,i.unit)
            scaleIngredients.append(scaleI)
        return Recipe(self.title,scaleIngredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ingredientsStr=",".join(str(i) for i in self.ingredients)
        if ingredientsStr:
            return f"{self.title}: {ingredientsStr}."
        else:
            return f"{self.title}."

