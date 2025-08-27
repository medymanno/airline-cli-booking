import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from airline_cli_project.models import Passenger, Flight, Booking, Base

@pytest.fixture(scope="function")
def session():
    """Create a new database for each test."""
    engine = create_engine("sqlite:///:memory:", echo=False)  # in-memory DB
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_can_create_passenger(session):
    passenger = Passenger(name="Flow Test", email="flow@test.com", passport_number="P999")
    session.add(passenger)
    session.commit()

    found = session.query(Passenger).filter_by(passport_number="P999").first()
    assert found is not None
    assert found.name == "Flow Test"

def test_can_book_flight(session):
    passenger = Passenger(name="Flow Book", email="book@test.com", passport_number="P888")
    flight = Flight(flight_number="ZZ999", origin="C", destination="D", available_seats=5)
    session.add_all([passenger, flight])
    session.commit()

    booking = Booking(passenger_id=passenger.id, flight_id=flight.id, seat_class="Economy")
    session.add(booking)
    session.commit()

    found = session.query(Booking).filter_by(seat_class="Economy").first()
    assert found is not None
    assert found.passenger_id == passenger.id
    assert found.flight_id == flight.id
