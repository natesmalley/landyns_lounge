# Meal Identification Microservice

This is a small FastAPI microservice that demonstrates how a system could
process meal images, retrieve recipes, generate grocery lists and compare
prices across providers. All logic uses very naive placeholder
implementations and the service should not be considered production ready.

## Setup

1. Install dependencies (requires Python 3.8+):

   ```bash
   pip install -r requirements.txt
   ```

2. Launch the service:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Upload a PPM image via the `/upload` endpoint to retrieve the detected
   meal, example recipes and a grocery list. Use `/compare` to obtain dummy
   pricing data from different providers.

This project is licensed under the Apache 2.0 license.
