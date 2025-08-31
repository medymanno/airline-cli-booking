from airline_cli_project.database import Base, engine, get_session, init_db
from airline_cli_project.models import Passenger, Flight

def seed_data():
    # Initialize DB tables
    init_db()
    session = get_session()

    # Clear existing data for a fresh start
    session.query(Passenger).delete()
    session.query(Flight).delete()
    session.commit()

    # Add passengers
    passengers = [
        Passenger(name="Alice Johnson", email="alice@example.com", passport_number="A1234567"),
        Passenger(name="Bob Smith", email="bob@example.com", passport_number="B7654321"),
    ]

    # Add flights
    flights = [
        Flight(flight_number="KQ101", origin="Nairobi", destination="London", available_seats=3),
        Flight(flight_number="EK202", origin="Dubai", destination="New York", available_seats=5),
        Flight(flight_number="ET303", origin="Addis Ababa", destination="Paris", available_seats=2),
    ]

    session.add_all(passengers + flights)
    session.commit()
    session.close()
    print("✅ Database seeded with sample passengers and flights!")

if __name__ == "__main__":
    seed_data()
