from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

from services.mock_db import MOCK_DASHBOARD_DATA

class MacroDetail(BaseModel):
    current: int
    target: int

class Macros(BaseModel):
    protein: MacroDetail
    carbs: MacroDetail
    fat: MacroDetail

class DashboardData(BaseModel):
    caloriesTarget: int
    caloriesConsumed: int
    macros: Macros


@router.get("/", response_model=DashboardData)
async def get_dashboard_data():
    """
    Get the aggregated data for the main dashboard.
    """
    return MOCK_DASHBOARD_DATA
