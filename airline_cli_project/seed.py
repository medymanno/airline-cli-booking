from airline_cli_project.models import Passenger, Flight, Booking
from airline_cli_project.database import get_session


# Create tables
Base.metadata.create_all(engine)

def seed_data():
    # Add passengers
    p1 = Passenger(name="Ahmed Mohamed", email="ahmed@example.com", passport_number="A12345")
    p2 = Passenger(name="Mary Ann", email="mary@example.com", passport_number="B67890")

    # Add flights
    f1 = Flight(flight_number="KQ101", origin="Nairobi", destination="London", available_seats=3)
    f2 = Flight(flight_number="ET202", origin="Addis Ababa", destination="Dubai", available_seats=2)
    f3 = Flight(flight_number="EK303", origin="Nairobi", destination="New York", available_seats=1)

    session.add_all([p1, p2, f1, f2, f3])
    session.commit()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
