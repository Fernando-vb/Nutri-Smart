# Shared mock data to ensure singleton behavior across routers

MOCK_DASHBOARD_DATA = {
  "caloriesTarget": 1800,
  "caloriesConsumed": 1200,
  "macros": {
    "protein": { "current": 90, "target": 140 },
    "carbs": { "current": 110, "target": 180 },
    "fat": { "current": 40, "target": 60 }
  }
}

MOCK_RECENT_FOODS = [
  { "id": 1, "name": "Pechuga de Pollo", "detail": "100g • 165 Kcal" },
  { "id": 2, "name": "Arroz Integral", "detail": "1 taza • 216 Kcal" },
  { "id": 3, "name": "Huevo Cocido", "detail": "1 unidad • 78 Kcal" },
  { "id": 4, "name": "Plátano", "detail": "1 unidad mediana • 105 Kcal" },
  { "id": 5, "name": "Batido Whey Protein", "detail": "1 scoop • 120 Kcal" },
  { "id": 6, "name": "Yogur Griego", "detail": "1 taza • 120 Kcal" },
]
