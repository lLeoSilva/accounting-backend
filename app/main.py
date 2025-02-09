from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, transactions, users

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

# Allow frontend requests (CORS policy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://api.hogarsantaelena.com", 
        "https://accounting.hogarsantaelena.com",
        "https://hogarsantaelena.com"
    ],  # Add both frontend and backend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, tags=["users"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])

# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
# app.include_router(users.router, prefix="", tags=["Users"])