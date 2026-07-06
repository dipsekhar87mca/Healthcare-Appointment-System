```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/patients")
def get_patients():
    return [
        {"id": 1, "name": "John Smith"},
        {"id": 2, "name": "Emma Wilson"}
    ]

@router.get("/doctors")
def get_doctors():
    return [
        {"id": 101, "name": "Dr. Amit Sharma", "specialization": "Cardiology"},
        {"id": 102, "name": "Dr. Sarah Thomas", "specialization": "Dermatology"}
    ]

@router.get("/appointments")
def get_appointments():
    return [
        {
            "appointmentId": 1001,
            "patient": "John Smith",
            "doctor": "Dr. Amit Sharma",
            "date": "2026-07-15",
            "status": "Confirmed"
        }
    ]

@router.post("/appointments")
def create_appointment():
    return {
        "message": "Appointment booked successfully."
    }
```
