import os
from dotenv import load_dotenv

load_dotenv()

origins = {
    "dev": [
        "http://localhost:3000",
        "https://localhost:3000",
    ],
    "prod": [
        "https://myProdSite",
    ]
}

class Base:
    env = os.getenv("ENVIRONMENT", "dev")
    name = os.getenv("NAME")
    url = os.getenv("URL")
    origins = origins.get(env)
