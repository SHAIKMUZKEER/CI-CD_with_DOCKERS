
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# 1. Create the FastAPI application
app = FastAPI(
    title="Multiplication Table Generator",
    description="Generate multiplication tables from 1 to 10.",
    version="1.0.0"
)


# 2. Configure CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# 3. Define and validate the request data
class TableRequest(BaseModel):
    number: float = Field(
        ge=-1_000_000,
        le=1_000_000,
        description="Number for generating the multiplication table"
    )


# 4. Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to the Multiplication Table API!",
        "status": "running",
        "docs": "/docs"
    }


# 5. Health-check route
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# 6. Generate multiplication table
@app.post("/table")
def generate_table(request: TableRequest):

    number = request.number

    table = []

    for multiplier in range(1, 11):
        result = number * multiplier

        table.append({
            "multiplier": multiplier,
            "result": result
        })

    return {
        "number": number,
        "table": table
    }


