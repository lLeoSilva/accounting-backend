from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, transactions

app = FastAPI()

# Allow frontend requests (CORS policy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include API routes
app.include_router(auth.router, prefix="/auth")
app.include_router(transactions.router, prefix="/transactions")