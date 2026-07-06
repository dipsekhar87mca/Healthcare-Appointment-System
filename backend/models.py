```python
from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    email: str

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str

class Appointment(BaseModel):
    appointmentId: int
    patientId: int
    doctorId: int
    appointmentDate: str
```
