# ✈️ Airline CLI Booking System
A simple **Command-Line Interface (CLI)** project for managing an airline booking system. Built with **Python** and **SQLAlchemy**, it allows you to manage **Passengers, Flights, and Bookings** from the terminal.

---

## 📌 Features
- Add and manage **Passengers** (name, email, passport number)
- Add and manage **Flights** (flight number, origin, destination, available seats)
- Create **Bookings** that link passengers to flights
- View existing data directly in the CLI
- Fully tested with `pytest`

---

## ⚙️ Installation & Setup
```bash
# 1️⃣ Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Set up the database
python airline_cli_project/seed.py

# ▶️ Usage
Run the CLI:
python airline_cli_project/cli.py
# You’ll be able to:
# - Add passengers
# - Add flights
# - Book a flight
# - View bookings

# 🧪 Running Tests
pytest -v


Ahmed (medymanno)
GitHub: @medymanno
