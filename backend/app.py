```python
from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Healthcare Appointment System API",
    description="Sample REST API for appointment management",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Healthcare Appointment System API",
        "status": "Running"
    }
```
