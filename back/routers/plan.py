from fastapi import APIRouter
from typing import List
from models.nutrition import Meal

router = APIRouter()

# Mock data from the frontend
MOCK_MEALS = [
  { "type": "Desayuno", "name": "Avena con proteína", "kcal": 450, "macros": "30P • 50C • 10G" },
  { "type": "Almuerzo", "name": "Pollo a la plancha y arroz", "kcal": 600, "macros": "45P • 60C • 15G" },
  { "type": "Snack", "name": "Manzana y almendras", "kcal": 200, "macros": "5P • 25C • 10G" },
  { "type": "Cena", "name": "Ensalada con atún", "kcal": 350, "macros": "35P • 10C • 15G" },
]

@router.get("/", response_model=List[Meal])
async def get_meal_plan():
    """
    Get the nutritional plan for the current user.
    This is currently mocked and would be generated based on user's profile.
    """
    return MOCK_MEALS
