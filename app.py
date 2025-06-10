from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class FlightBook(BaseModel):
    name : str
    from_city : str
    to_city : str
    travel_date : date
    passengers : int

class BookingResponse(BaseModel):
    message : str
    booking_id : str
    status : str

@app.post("/book-flight", response_model = BookingResponse)
def book_flight(request: FlightBook):
    booking_id = f"BOOK-{request.name[:3].upper()}-{request.travel_date.strftime('%d%m%Y')}"
    return BookingResponse(
        message = f"Hi {request.name}, your flight from {request.from_city} to {request.to_city}"
        f" on {request.travel_date} for {request.passengers} passenger(s) has been booked.",
        booking_id=booking_id,
        status="Confirmed"
    )