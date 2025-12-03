@echo off
echo Starting Nutri-Smart...

:: Start Backend
start "Nutri-Smart Backend" cmd /k "cd back && echo Installing dependencies... && pip install -r requirements.txt && echo Starting Server... && uvicorn main:app --reload"

:: Start Frontend
start "Nutri-Smart Frontend" cmd /k "cd front && echo Installing dependencies... && npm install && echo Starting Dev Server... && npm run dev"

echo Servers are starting in new windows.
