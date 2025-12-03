# Nutri-Smart

## Prerequisites
- Python 3.x
- Node.js

## How to Run

### Backend
1. Open a terminal.
2. Navigate to the `back` folder:
   ```bash
   cd back
   ```
3. Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

### Frontend
1. Open a new terminal.
2. Navigate to the `front` folder:
   ```bash
   cd front
   ```
3. Install dependencies (if not already installed):
   ```bash
   npm install
   ```
4. Run the development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173`.

## Quick Start (Windows)
You can run the `start_all.bat` script to open both servers in new terminal windows automatically.
