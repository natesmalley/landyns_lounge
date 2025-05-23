from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from .classifier import MealClassifier
from .recipes import RecipeFinder
from .grocery import GroceryListBuilder
from .providers import ProviderClient

app = FastAPI(title="Meal Identification Service")

# Initialize components
classifier = MealClassifier()
recipes = RecipeFinder()
grocery_builder = GroceryListBuilder()
provider_client = ProviderClient()


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    data = await file.read()
    meal_type = classifier.classify(data)
    similar = classifier.verify_with_similar_images(data)
    if not similar:
        return JSONResponse(status_code=400, content={"error": "Meal could not be verified"})

    recipe_list = recipes.find_recipes(meal_type)
    grocery_list = grocery_builder.build_grocery_list(recipe_list)

    return {
        "meal_type": meal_type,
        "recipes": recipe_list,
        "grocery_list": grocery_list,
    }


@app.post("/compare")
async def compare_prices(grocery_list: dict):
    prices = provider_client.compare_prices(grocery_list)
    return prices
