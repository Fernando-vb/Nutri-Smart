from fastapi import APIRouter
from typing import List
from models.nutrition import HistoryDay

router = APIRouter()

# Mock data from the frontend
MOCK_HISTORY = [
  { "date": "Hoy", "calories": 1200, "target": 1800, "status": "inprogress" },
  { "date": "Ayer", "calories": 1750, "target": 1800, "status": "success" },
  { "date": "20 Nov", "calories": 2100, "target": 1800, "status": "warning" },
  { "date": "19 Nov", "calories": 1800, "target": 1800, "status": "success" },
  { "date": "18 Nov", "calories": 1650, "target": 1800, "status": "success" },
]

@router.get("/", response_model=List[HistoryDay])
async def get_history():
    """
    Get the consumption history for the current user.
    """
    return MOCK_HISTORY
