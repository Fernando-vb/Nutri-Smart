from fastapi import APIRouter
from typing import List
from models.nutrition import Notification

router = APIRouter()

# Mock data
MOCK_NOTIFICATIONS = [
    {
        "id": 1,
        "type": "alert",
        "title": "Recordatorio de Hidratación",
        "time": "Hace 10 min",
        "description": "No olvides beber tu vaso de agua de las 10:00 AM.",
        "isRead": False
    },
    {
        "id": 2,
        "type": "goal",
        "title": "¡Meta Alcanzada!",
        "time": "Hace 2 horas",
        "description": "Felicidades, has completado tu objetivo de proteínas del día.",
        "isRead": True
    }
]

@router.get("/", response_model=List[Notification])
async def get_notifications():
    """
    Get all notifications for the current user.
    """
    return MOCK_NOTIFICATIONS
