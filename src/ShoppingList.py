from src.Ingredient import Ingredient
class ShoppingList:
    def __init__(self):
        self._items=[]

    def add_recipe(self,recipe: "Recipe", portions: float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        scaleRecipe=recipe.scale(portions)
        for i in scaleRecipe.ingredients:
            self._items.append((i,recipe.title))

    def remove_recipe(self,title: str):
        self._items=[item for item in self._items if item[1]!=title]

    def get_list(self):
        aggregatedIngredients={}
        for i, _ in self._items:
            key=(i.name,i.unit)
            if key in aggregatedIngredients:
                aggregatedIngredients[key]+=i.quantity
            else:
                aggregatedIngredients[key]=i.quantity
        result=[]
        for (name,unit), totQuantity in aggregatedIngredients.items():
            result.append(Ingredient(name, totQuantity,unit))
        return sorted(result,key=lambda i:i.name)

    def __add__(self, other: "ShoppingList"):
        if not isinstance(other,ShoppingList):
            return NotImplemented
        list2=ShoppingList()
        list2._items=self._items.copy()
        list2._items.extend(other._items)
        return list2




