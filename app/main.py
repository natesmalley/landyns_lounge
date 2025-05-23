from fastapi import FastAPI, Request
import sitecustomize  # ensure httpx patch applied
from fastapi.responses import JSONResponse
from email.parser import BytesParser
from email.policy import default
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
async def upload_image(request: Request):
    content_type = request.headers.get("content-type", "")
    body = await request.body()
    message = BytesParser(policy=default).parsebytes(
        b"Content-Type: " + content_type.encode() + b"\n\n" + body
    )
    file_bytes = None
    for part in message.iter_parts():
        disposition = part.get("Content-Disposition", "")
        if "name=\"file\"" in disposition:
            file_bytes = part.get_payload(decode=True)
            break
    if file_bytes is None:
        return JSONResponse(status_code=400, content={"error": "File not found"})

    meal_type = classifier.classify(file_bytes)
    similar = classifier.verify_with_similar_images(file_bytes)
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
