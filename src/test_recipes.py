import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList

# ДЛЯ INGREDIENT
def testIngredientCreative():
    ingredient=Ingredient("Мука",500.0,"г")
    assert ingredient.name=="Мука"
    assert ingredient.quantity==500.0
    assert ingredient.unit=="г"

def testStr():
    ingredient=Ingredient("Мука",500.0,"г")
    assert str(ingredient)=="Мука: 500.0 г"

def testEqualNameUnit():
    ingredient1=Ingredient("Мука",500.0,"г")
    ingredient2=Ingredient("Мука",1000.0,"г")
    assert ingredient1==ingredient2

def testEqualDiffName():
    ingredient1=Ingredient("Мука",500.0,"г")
    ingredient2=Ingredient("Сахар",500.0,"г")
    assert ingredient1!=ingredient2

def testEqualDiffUnit():
    ingredient1=Ingredient("Мука",500.0,"г")
    ingredient2=Ingredient("Мука",500.0,"кг")
    assert ingredient1!=ingredient2


# ДЛЯ RECIPE
def testRecipeCreative():
    ingredient=[Ingredient("Мука",500.0,"г")]
    recipe=Recipe("Хлеб", ingredient)
    assert recipe.title=="Хлеб"
    assert recipe.ingredients==ingredient

def testAddIngredient():
    recipe=Recipe("Хлеб")
    ingredient=Ingredient("Мука",500.0,"г")
    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients)==1
    assert recipe.ingredients[0]==ingredient

def testAddIngrSumQuantity():
    recipe =Recipe("Хлеб",[Ingredient("Мука",200.0,"г")])
    recipe.add_ingredient(Ingredient("Мука",500.0,"г"))
    assert len(recipe.ingredients)==1
    assert recipe.ingredients[0].quantity==700.0

def testScaleReturnNew():
    recipe=Recipe("Хлеб", [Ingredient("Мука",500.0,"г")])
    scaleRecipe=recipe.scale(2)
    assert scaleRecipe is not recipe
    assert isinstance(scaleRecipe,Recipe)

def testScaleMultiQua():
    recipe=Recipe("Хлеб", [Ingredient("Мука",500.0,"г"), Ingredient("Вода",300,"мл")])
    scaleRecipe=recipe.scale(2)
    assert scaleRecipe.ingredients[0].quantity==1000
    assert scaleRecipe.ingredients[1].quantity==600

def testScaleNotChangeOriginal():
    recipe=Recipe("Хлеб", [Ingredient("Мука",500.0,"г")])
    scaleRecipe=recipe.scale(2)
    assert recipe.ingredients[0].quantity==500
    assert scaleRecipe.ingredients[0].quantity==1000

def testScaleValueError():
    recipe=Recipe("Хлеб")
    with pytest.raises(ValueError):
        recipe.scale(0)

def testScaleValueError2():
    recipe=Recipe("Хлеб")
    with pytest.raises(ValueError):
        recipe.scale(-67)

def testLenReturnNum():
    recipe=Recipe("Хлеб", [Ingredient("Мука",500.0,"г"), Ingredient("Вода",300,"мл")])
    assert len(recipe)==2


# ДЛЯ SHOPPINGLIST
def testAddRecipe():
    recipe = Recipe("Блины", [Ingredient("Мука", 100.0, "г")])
    shoppingList=ShoppingList()
    shoppingList.add_recipe(recipe,1)
    result=shoppingList.get_list()
    assert len(result)==1
    assert result[0].name=="Мука"
    assert result[0].quantity==100.0

def testInvalidPortions():
    recipe = Recipe("Блины")
    shoppingList=ShoppingList()
    with pytest.raises(ValueError):
        shoppingList.add_recipe(recipe,0)

def testRemoveRecipe():
    recipe1 = Recipe("Блины", [Ingredient("Мука", 100.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Яйца", 3, "шт")])
    shoppingList=ShoppingList()
    shoppingList.add_recipe(recipe1,1)
    shoppingList.add_recipe(recipe2,1)
    shoppingList.remove_recipe("Блины")
    result=shoppingList.get_list()
    assert len(result)==1
    assert result[0].name=="Яйца"

def testRemoveEmptyRecipe():
    shoppingList=ShoppingList()
    shoppingList.remove_recipe("Не существует")
    assert shoppingList.get_list()==[]

def testSumOfSameIngr():
    recipe1 = Recipe("Блины", [Ingredient("Мука", 100.0, "г")])
    recipe2 = Recipe("Приог", [Ingredient("Мука", 200.0, "г")])
    shoppingList=ShoppingList()
    shoppingList.add_recipe(recipe1,1)
    shoppingList.add_recipe(recipe2,1)
    result= shoppingList.get_list()
    assert len(result)==1
    assert result[0].name=="Мука"
    assert result[0].quantity==300.0

def testSoertedName():
    recipe=Recipe("Тест", [Ingredient("Яйца",2,"шт"),Ingredient("Мука",100.0,"г")])
    shoppingList= ShoppingList()
    shoppingList.add_recipe(recipe,1)
    result=shoppingList.get_list()
    assert result[0].name=="Мука"
    assert result[1].name=="Яйца"

def testAddComba():
    recipe1 = Recipe("Блины", [Ingredient("Мука", 100.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Яйца", 3, "шт")])
    list1=ShoppingList()
    list2=ShoppingList()
    list1.add_recipe(recipe1,1)
    list2.add_recipe(recipe2,1)
    comba=list1+list2
    result=comba.get_list()
    assert len(result)==2

def testOriginalsNotChange():
    recipe1 = Recipe("Блины", [Ingredient("Мука", 100.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Яйца", 3, "шт")])
    list1 = ShoppingList()
    list2 = ShoppingList()
    list1.add_recipe(recipe1, 1)
    list2.add_recipe(recipe2, 1)
    comba = list1 + list2
    assert len(list1.get_list())==1
    assert len(list2.get_list())==1
    assert len(comba.get_list())==2


