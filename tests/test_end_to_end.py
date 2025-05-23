from fastapi.testclient import TestClient
from PIL import Image
import io

from app.main import app

client = TestClient(app)


def test_upload_and_compare():
    # Create a dummy image simulating spaghetti bolognese
    img = Image.new("RGB", (10, 10), color=(255, 0, 0))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    response = client.post(
        "/upload",
        files={"file": ("spaghetti.png", buf, "image/png")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["meal_type"] == "pizza"  # stub classifier always returns pizza
    assert isinstance(data["recipes"], list)
    assert isinstance(data["grocery_list"], dict)

    response = client.post("/compare", json=data["grocery_list"])
    assert response.status_code == 200
    prices = response.json()
    assert set(prices.keys()) == {"uber_eats", "safeway", "walmart"}
