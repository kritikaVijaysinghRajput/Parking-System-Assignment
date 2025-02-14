
---

# Parking Management System

## Overview

This project is a Parking Management System with a backend built using Django and a frontend built using React. The system allows users to manage vehicle parking sessions, including check-in and check-out functionalities. Users can view details of their vehicles, including check-in and check-out times, and the total amount due.

## Features

- User Authentication: Users can log in to the system.
- Vehicle Management: Users can check in and check out vehicles.
- Real-time Updates: The list of currently parked vehicles is dynamically updated.
- Detailed Vehicle Information: Users can view detailed information about each vehicle, including check-in time, check-out time, and total amount due.

## Models

### Vehicle

A custom model for vehicle details:

- **Number**: License Plate
- **Make**: Manufacturer
- **Model**: Model of the vehicle

### User

The standard Django user model, extended as needed.

### ParkingSession

A model to track the parking sessions:

- **Vehicle**: ForeignKey to the Vehicle model
- **User**: ForeignKey to the User model
- **Check-in Time**: DateTimeField
- **Check-out Time**: DateTimeField (calculated at checkout)
- **Total Amount Due**: DecimalField (calculated at checkout)

## Relationships

- A user can have multiple vehicles.
- A vehicle can have multiple parking sessions.

## Views

### Login Page

Form for existing users to log in.

### Home Page

- Form for checking in and checking out vehicles.
- Display a list of currently parked vehicles.
- On click, display detailed vehicle information and the option to check out.

## Functionalities

- **Real-time Vehicle List Update**: The list of vehicles is dynamically updated to reflect the current state.
- **Check-in and Check-out**: Users can check in vehicles and receive a receipt upon checking out, including the total amount due.

## Installation

### Backend (Django)

1. **Clone the repository**:
   ```bash
  [ git clone https://github.com/repo/parking-management-system.git](https://github.com/kritikaVijaysinghRajput/Parking-System-Assignment)
   cd folder
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

### Frontend (React)

1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```

## API Endpoints

- **/api/login/**: User login
- **/api/vehicles/**: List and create vehicles
- **/api/vehicles/{id}/**: Retrieve, update, or delete a vehicle
- **/api/parking-sessions/**: List and create parking sessions
- **/api/parking-sessions/{id}/**: Retrieve, update, or delete a parking session
- **/api/active-vehicles/**: List currently active parking sessions (checked-in vehicles)
- **/api/checkout/**: Checkout a vehicle

## Usage

1. **Login**: Use the login form to authenticate.
2. **Check-in Vehicle**: Use the form on the home page to check in a vehicle.
3. **View Vehicles**: See the list of currently parked vehicles on the home page.
4. **Check-out Vehicle**: Click on a vehicle to view details and check out.

## Screenshots

### Login Page

![Login Page]![screencapture-parking-frontend-six-vercel-app-2024-07-15-19_41_51](https://github.com/user-attachments/assets/31ff891b-4e31-4321-8535-edeabaf5ed59)



### Home Page

![Home Page]![screencapture-parking-frontend-six-vercel-app-home-2024-07-15-19_34_03](https://github.com/user-attachments/assets/8771f61a-5e0e-4593-9b96-6da88b1cf3a8)




## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.

---

### sample user 
{
 "username": "john_doe",
 "password": "password123"
} 

### deployed links

Frontend : https://parking-frontend-six.vercel.app/

Backend : https://parking-system-api.onrender.com/

---

Kritika Rajput
Email : kritikarajput203@gmail.com

