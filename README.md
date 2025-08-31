# ✈️ Airline CLI Booking System

A simple **Command-Line Interface (CLI)** project for managing an airline booking system.  
Built with **Python** and **SQLAlchemy**, it allows you to manage **Passengers, Flights, and Bookings** from the terminal.

## 📌 Features

- ✅ Add and manage **Passengers** (name, email, passport number)
- ✅ Add and manage **Flights** (flight number, origin, destination, available seats)
- ✅ Create **Bookings** that link passengers to flights
- ✅ View existing data directly in the CLI
- ✅ Fully tested with `pytest`
- ✅ SQLite database with SQLAlchemy ORM

## 🛠️ Tech Stack

- **Python 3.12+**
- **SQLAlchemy** - Database ORM
- **SQLite** - Database
- **Pytest** - Testing framework

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd airline_cli_project
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
# venv\Scripts\activate    # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install pipenv
pipenv install
```

**Or using pip directly:**
```bash
pip install sqlalchemy pytest
```

### 4️⃣ Set up the database
```bash
python airline_cli_project/seed.py
```

## ▶️ Usage

### Run the CLI application:
```bash
python airline_cli_project/cli.py
```

### Available Operations:
1. **Add Passenger** - Register new passengers with personal details
2. **Add Flight** - Create new flights with route and capacity information
3. **Book Flight** - Link passengers to available flights
4. **View Bookings** - Display all current bookings
5. **Exit** - Close the application

### Example Workflow:
```bash
$ python airline_cli_project/cli.py

=== Airline Booking System ===
1. Add Passenger
2. Add Flight
3. Book Flight
4. View Bookings
5. Exit

Choose an option: 1
Enter passenger name: John Doe
Enter email: john@example.com
Enter passport number: AB123456
✅ Passenger added successfully!
```

## 🧪 Running Tests

Run all tests:
```bash
pytest -v
```

Run specific test files:
```bash
pytest airline_cli_project/tests/test_models.py -v
pytest airline_cli_project/tests/test_booking_flow.py -v
```


## 🗄️ Database Schema

### Models:
- **Passenger**: `id`, `name`, `email`, `passport_number`
- **Flight**: `id`, `flight_number`, `origin`, `destination`, `available_seats`
- **Booking**: `id`, `passenger_id`, `flight_id`, `booking_date`

### Relationships:
- One passenger can have multiple bookings
- One flight can have multiple bookings
- Each booking links one passenger to one flight

## 🚀 Future Improvements

- [ ] Add search/filter functionality for flights
- [ ] Implement booking cancellation and updates
- [ ] Support for different databases (PostgreSQL, MySQL)
- [ ] Enhanced CLI UX with better menus and navigation
- [ ] Add flight scheduling and time management
- [ ] Implement seat selection functionality
- [ ] Add booking confirmation emails
- [ ] Create a web interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Ahmed (medymanno)**
- GitHub: [@medymanno](https://github.com/medymanno)

---
