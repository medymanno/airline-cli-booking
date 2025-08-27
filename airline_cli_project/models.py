from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from airline_cli_project.database import Base
from datetime import datetime, timezone  # updated import

class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    passport_number = Column(String, unique=True)

    bookings = relationship("Booking", back_populates="passenger")

    def __repr__(self):
        return f"<Passenger(name={self.name}, email={self.email}, passport={self.passport_number})>"


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    flight_number = Column(String, unique=True)
    origin = Column(String)
    destination = Column(String)
    available_seats = Column(Integer)

    bookings = relationship("Booking", back_populates="flight")

    def __repr__(self):
        return f"<Flight({self.flight_number}, {self.origin} → {self.destination}, seats={self.available_seats})>"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey("passengers.id"))
    flight_id = Column(Integer, ForeignKey("flights.id"))
    seat_class = Column(String)  # Economy / Business
    booked_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # fixed

    passenger = relationship("Passenger", back_populates="bookings")
    flight = relationship("Flight", back_populates="bookings")

    def __repr__(self):
        return f"<Booking(passenger={self.passenger_id}, flight={self.flight_id}, class={self.seat_class})>"
