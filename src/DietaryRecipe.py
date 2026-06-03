from src.Recipe import Recipe
class DietaryRecipe(Recipe) :
    def __init__(self, title:str,diet_type:str,ingredients=None):
        super().__init__(title,ingredients)
        self.diet_type=diet_type

    def scale(self,ratio:float):
        scaleRecipe=super().scale(ratio)
        return DietaryRecipe(scaleRecipe.title,self.diet_type,scaleRecipe.ingredients)

    def __str__(self):
        parentStr=super().__str__()
        return f"[{self.diet_type}] {parentStr}"
