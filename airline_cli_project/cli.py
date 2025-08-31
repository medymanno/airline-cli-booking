from airline_cli_project.models import Passenger, Flight, Booking
from airline_cli_project.database import get_session


def menu():
    while True:
        print("\n✈️ Airline Ticket Booking CLI")
        print("1. View available flights")
        print("2. Book a ticket")
        print("3. Cancel a booking")
        print("4. View my bookings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_flights()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")


def view_flights():
    session = get_session()
    flights = session.query(Flight).all()
    if flights:
        for f in flights:
            print(f"{f.id}. {f.flight_number}: {f.origin} → {f.destination} (Seats: {f.available_seats})")
    else:
        print("No flights available.")
    session.close()


def book_ticket():
    session = get_session()
    try:
        passenger_id = int(input("Enter your Passenger ID: "))
        flight_id = int(input("Enter Flight ID to book: "))
        seat_class = input("Enter seat class (Economy/Business): ")

        passenger = session.get(Passenger, passenger_id)
        flight = session.get(Flight, flight_id)

        if passenger and flight and flight.available_seats > 0:
            booking = Booking(passenger_id=passenger.id, flight_id=flight.id, seat_class=seat_class)
            flight.available_seats -= 1
            session.add(booking)
            session.commit()
            print(f"✅ Ticket booked for {passenger.name} on {flight.flight_number} ({seat_class})")
        else:
            print("❌ Booking failed. Check Passenger/Flight ID or seat availability.")
    except ValueError:
        print("❌ Invalid input. Please enter valid IDs.")
    finally:
        session.close()


def cancel_booking():
    session = get_session()
    try:
        booking_id = int(input("Enter Booking ID to cancel: "))
        booking = session.get(Booking, booking_id)

        if booking:
            flight = booking.flight
            flight.available_seats += 1
            session.delete(booking)
            session.commit()
            print(f"✅ Booking {booking_id} cancelled. Seat returned to flight {flight.flight_number}.")
        else:
            print("❌ Booking not found.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid Booking ID.")
    finally:
        session.close()


def view_bookings():
    session = get_session()
    try:
        passenger_id = int(input("Enter your Passenger ID: "))
        bookings = session.query(Booking).filter_by(passenger_id=passenger_id).all()

        if bookings:
            for b in bookings:
                print(f"Booking {b.id}: Flight {b.flight.flight_number} ({b.flight.origin} → {b.flight.destination}), "
                      f"Class: {b.seat_class}, Date: {b.booked_at}")
        else:
            print("No bookings found for this passenger.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid Passenger ID.")
    finally:
        session.close()


if __name__ == "__main__":
    menu()
