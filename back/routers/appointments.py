from fastapi import APIRouter, Body
from typing import Optional
from models.nutrition import Appointment

router = APIRouter()

# Mock data - In a real app this would be in a database
# We'll use a simple global variable to simulate persistence for the session
next_appointment: Optional[Appointment] = None

@router.get("/", response_model=Optional[Appointment])
async def get_next_appointment():
    """
    Get the next scheduled appointment.
    """
    return next_appointment

@router.post("/", response_model=Appointment)
async def schedule_appointment(appointment: Appointment):
    """
    Schedule a new appointment.
    """
    global next_appointment
    next_appointment = appointment
    return appointment
