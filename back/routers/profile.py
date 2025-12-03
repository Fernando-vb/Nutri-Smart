from fastapi import APIRouter, Depends, HTTPException, status
from models.nutrition import NutritionProfile
# from services.profile_service import get_user_profile, update_user_profile
# from depends.get_current_user import get_current_active_user # Assuming dependency for user auth

router = APIRouter()

# Mock profile database for demonstration
MOCK_PROFILE_DB = {
    "carla.fit@smartfit.com": {
        "goal": "Perder peso",
        "weight": 70.5,
        "height": 170,
        "age": 28,
        "sex": "Femenino",
        "activityLevel": "Moderado",
        "allergies": ["Lactosa"]
    }
}

@router.get("/", response_model=NutritionProfile)
async def get_profile():
    """
    Get the nutrition profile for the current user.
    In a real app, user would be identified from a token.
    """
    # Hardcoding user for now, would come from Depends(get_current_active_user)
    user_email = "carla.fit@smartfit.com" 
    profile = MOCK_PROFILE_DB.get(user_email)
    
    if not profile:
        # Return a default or empty profile if none exists
        return NutritionProfile(
            goal='No definido', 
            weight=0, 
            height=0, 
            age=0, 
            sex='No definido', 
            activityLevel='No definido', 
            allergies=[]
        )
    return profile

@router.post("/", response_model=NutritionProfile)
async def create_or_update_profile(profile_data: NutritionProfile):
    """
    Create or update the nutrition profile for the current user.
    """
    # Hardcoding user for now
    user_email = "carla.fit@smartfit.com"
    MOCK_PROFILE_DB[user_email] = profile_data.dict()
    return MOCK_PROFILE_DB[user_email]
