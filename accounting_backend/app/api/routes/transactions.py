from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Transaction
from app.schemas.schemas import TransactionCreate, TransactionOut

router = APIRouter()

@router.post("/", response_model=TransactionOut)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    new_transaction = Transaction(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    return new_transaction

@router.get("/", response_model=list[TransactionOut])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()