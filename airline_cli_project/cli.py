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
    flights = session.query(Flight).all()
    for f in flights:
        print(f"{f.id}. {f.flight_number}: {f.origin} → {f.destination} (Seats: {f.available_seats})")

def book_ticket():
    passenger_id = int(input("Enter your Passenger ID: "))
    flight_id = int(input("Enter Flight ID to book: "))
    seat_class = input("Enter seat class (Economy/Business): ")

    passenger = session.query(Passenger).get(passenger_id)
    flight = session.query(Flight).get(flight_id)

    if passenger and flight and flight.available_seats > 0:
        booking = Booking(passenger_id=passenger.id, flight_id=flight.id, seat_class=seat_class)
        flight.available_seats -= 1
        session.add(booking)
        session.commit()
        print(f"✅ Ticket booked for {passenger.name} on {flight.flight_number} ({seat_class})")
    else:
        print("❌ Booking failed. Check Passenger/Flight ID or seats availability.")

def cancel_booking():
    booking_id = int(input("Enter Booking ID to cancel: "))
    booking = session.query(Booking).get(booking_id)

    if booking:
        flight = booking.flight
        flight.available_seats += 1
        session.delete(booking)
        session.commit()
        print(f"✅ Booking {booking_id} cancelled. Seat returned to flight {flight.flight_number}.")
    else:
        print("❌ Booking not found.")

def view_bookings():
    passenger_id = int(input("Enter your Passenger ID: "))
    bookings = session.query(Booking).filter_by(passenger_id=passenger_id).all()

    if bookings:
        for b in bookings:
            print(f"Booking {b.id}: Flight {b.flight.flight_number} ({b.flight.origin} → {b.flight.destination}), "
                  f"Class: {b.seat_class}, Date: {b.booked_at}")
    else:
        print("No bookings found for this passenger.")

if __name__ == "__main__":
    menu()
