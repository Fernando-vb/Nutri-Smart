from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar routers
from routers.auth import router as auth_router
from routers.profile import router as profile_router
from routers.vision import router as vision_router
from routers.plan import router as plan_router
from routers.history import router as history_router
from routers.food import router as food_router
from routers.dashboard import router as dashboard_router
from routers.notifications import router as notifications_router
from routers.appointments import router as appointments_router

app = FastAPI(
    title="Nutri-Smart API",
    version="1.0",
    description="API para la aplicación de nutrición Nutri-Smart"
)

# --- Middlewares ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(profile_router, prefix="/api/v1/profile", tags=["Profile"])
app.include_router(vision_router, prefix="/api/v1/vision", tags=["Vision"])
app.include_router(plan_router, prefix="/api/v1/plan", tags=["Plan"])
app.include_router(history_router, prefix="/api/v1/history", tags=["History"])
app.include_router(food_router, prefix="/api/v1/food", tags=["Food"])
app.include_router(dashboard_router, prefix="/api/v1/dashboard", tags=["Dashboard"])
app.include_router(notifications_router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(appointments_router, prefix="/api/v1/appointments", tags=["Appointments"])


@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Welcome to Nutri-Smart API"}

