from airline_cli_project.models import Passenger, Flight, Booking

def test_passenger_repr():
    p = Passenger(name="Test", email="test@test.com", passport_number="P123")
    assert "Test" in str(p)

def test_flight_repr():
    f = Flight(flight_number="AB123", origin="A", destination="B", available_seats=10)
    assert "AB123" in str(f)

def test_booking_repr():
    b = Booking(passenger_id=1, flight_id=2, seat_class="Economy")
    assert "Economy" in str(b)
def test_math_works():
    assert 1 + 1 == 2
