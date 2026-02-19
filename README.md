# Hotel Management & Online Booking System

## Project Overview
This project is a full-stack Hotel Management and Online Room Booking System. It allows users to book hotel rooms online by selecting room type, number of rooms, number of guests, arrival date, and departure date. All booking details are stored securely in a cloud database.

## Features
- Online room booking form
- Arrival and departure date selection
- Multiple user booking support
- Cloud database storage
- Flask REST API backend

## Technologies Used
- HTML, CSS, JavaScript (Frontend)
- Flask (Python Backend)
- PostgreSQL (Neon Cloud Database)
- Render (Backend Deployment)

## How the System Works
1. User fills the booking form on the website.
2. Form data is sent to the Flask backend using Fetch API.
3. Flask processes the request and stores data in PostgreSQL cloud database.
4. Booking information is stored permanently and securely.

## Deployment Details
The backend of this project is deployed using Render cloud platform. The database is hosted on Neon PostgreSQL cloud service. Sensitive information such as database credentials is stored securely using environment variables like DATABASE_URL.

## Database Structure
- id (Primary Key)
- name
- email
- room_type
- num_rooms
- num_guests
- arrival_date
- departure_date

## Future Enhancements
- Admin dashboard to view all bookings
- Booking history for users
- Payment gateway integration
- Email booking confirmation system

## Author
This project was developed as a learning project to understand full-stack web development, backend integration, and cloud deployment.
