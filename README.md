# ✈️ Airline CLI Booking System

# A simple Command-Line Interface (CLI) project for managing an airline booking system.  
# Built with Python and SQLAlchemy, it allows you to manage Passengers, Flights, and Bookings from the terminal.

# -----------------------------------------------------------
# Features
# -----------------------------------------------------------
# - Add and manage Passengers (name, email, passport number)
# - Add and manage Flights (flight number, origin, destination, available seats)
# - Create Bookings that link passengers to flights
# - View existing data directly in the CLI
# - Fully tested with pytest

# -----------------------------------------------------------
# Installation & Setup
# -----------------------------------------------------------

# 1️ Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# 2️ Install dependencies
pip install -r requirements.txt

# 3️ Set up the database
python airline_cli_project/seed.py

# -----------------------------------------------------------
#  Usage
# -----------------------------------------------------------
python airline_cli_project/cli.py

# You’ll be able to:
# - Add passengers
# - Add flights
# - Book a flight
# - View bookings

# -----------------------------------------------------------
# Running Tests
# -----------------------------------------------------------
pytest -v

# -----------------------------------------------------------
#  Project Structure
# -----------------------------------------------------------
# airline_cli_project/
# │── cli.py          # Main CLI entry point
# │── database.py     # Database setup and session handling
# │── models.py       # SQLAlchemy models (Passenger, Flight, Booking)
# │── seed.py         # Seeds the database with sample data
# │── tests/          # Pytest test cases
# │
# ├── airline.db      # SQLite database (auto-created)
# ├── README.md       # Project documentation
# ├── Pipfile         # Pipenv dependencies (optional)
# └── requirements.txt# Python dependencies

# -----------------------------------------------------------
#  Future Improvements
# -----------------------------------------------------------
# - Add search/filter for flights
# - Cancel or update bookings
# - Support for different databases (PostgreSQL, MySQL)
# - Improve CLI UX with menus

# -----------------------------------------------------------
# Author
# -----------------------------------------------------------
# Ahmed (medymanno)
# GitHub: @medymanno
