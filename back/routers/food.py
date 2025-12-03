from fastapi import APIRouter, Body
from typing import List
from pydantic import BaseModel
from models.nutrition import FoodItem

router = APIRouter()

from services.mock_db import MOCK_RECENT_FOODS, MOCK_DASHBOARD_DATA

@router.get("/recent", response_model=List[FoodItem])
async def get_recent_foods():
    """
    Get the user's recently logged food items.
    """
    return MOCK_RECENT_FOODS

class LogFoodRequest(BaseModel):
    food_name: str
    calories: int = 300

@router.post("/log", response_model=FoodItem)
async def log_food(request: LogFoodRequest):
    """
    Logs a new food item.
    """
    new_id = max(food["id"] for food in MOCK_RECENT_FOODS) + 1 if MOCK_RECENT_FOODS else 1
    
    # Use provided calories or default
    estimated_calories = request.calories
    
    new_food = FoodItem(id=new_id, name=request.food_name, detail=f"1 porción • {estimated_calories} Kcal")
    
    # Add to the top of the list
    MOCK_RECENT_FOODS.insert(0, new_food.dict())
        
    MOCK_DASHBOARD_DATA["caloriesConsumed"] += estimated_calories
    
    # Update macros (mock logic)
    MOCK_DASHBOARD_DATA["macros"]["protein"]["current"] += 20
    MOCK_DASHBOARD_DATA["macros"]["carbs"]["current"] += 30
    MOCK_DASHBOARD_DATA["macros"]["fat"]["current"] += 10
    
    return new_food
