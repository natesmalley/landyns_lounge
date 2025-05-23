# Meal Identification Microservice

This is a sample FastAPI microservice that demonstrates how a system could
process meal images, retrieve recipes, generate grocery lists, and compare
prices across providers.

The core logic is simplified and uses lightweight heuristics. The image
classifier estimates the meal type by comparing the average image color against
predefined signatures for common meals. Recipe and pricing data are static or
randomly generated. Replace these components with real image recognition
models, recipe APIs, and provider integrations for production use.

## Setup

1. Install dependencies (requires Python 3.8+):

   ```bash
   pip install -r requirements.txt
   ```

   The first run may attempt to download model weights if using real
   image recognition libraries.

2. Launch the service:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Upload an image via the `/upload` endpoint to retrieve the detected meal,
   example recipes, and a grocery list. Use `/compare` to obtain dummy pricing
   data from different providers.

This project is licensed under the Apache 2.0 license.
