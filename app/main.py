from fastapi import FastAPI, Request
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


def _extract_file(content_type: str, body: bytes) -> bytes:
    """Return the first file content from a multipart/form-data body."""

    msg = BytesParser(policy=default).parsebytes(
        b"Content-Type: " + content_type.encode() + b"\n\n" + body
    )
    if not msg.is_multipart():
        raise ValueError("Not a multipart request")
    for part in msg.iter_parts():
        if part.get_filename():
            return part.get_payload(decode=True)
    raise ValueError("No file part found")


@app.post("/upload")
async def upload_image(request: Request):
    content_type = request.headers.get("content-type", "")
    body = await request.body()
    try:
        data = _extract_file(content_type, body)
    except Exception:
        return JSONResponse(status_code=400, content={"error": "Invalid upload"})

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
