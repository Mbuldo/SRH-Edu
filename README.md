# Healthy Sex, Healthy Life

An STI Awareness Web Application providing accurate, stigma-free information about sexual health among university students.

## Description

This web application aims to educate users about Sexual and Reproductive Health through:
- Educational content about STIs and Reproductive health
- Interactive symptom checker
- FAQs
- Clinic locator for healthcare services in Nairobi
- Admin panel for content management

## Problem

Many people lack access to accurate, stigma-free information about STIs and sexual health. This leads to:
- Delayed treatment seeking
- Spread of misinformation
- Stigma around STIs
- Poor health outcomes

## Solution

Our web application provides:
- Accessible, accurate information
- Anonymous symptom checking
- Easy clinic finding
- Interactive learning through quizzes
- Regular health tips and updates

##Video Demo

https://www.loom.com/share/2fd5cf816eaa42cab956bf3afe064183?sid=f9becd7c-c2ea-43da-99fc-065481a9cf0a

##Screenshots

/home/micah/Pictures/Screenshots/Screenshot From 2025-10-13 17-09-41.png
/home/micah/Pictures/Screenshots/Screenshot From 2025-10-13 17-10-11.png
/home/micah/Pictures/Screenshots/Screenshot From 2025-10-13 17-11-10.png

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for frontend development)
- Git

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/Mbuldo/SRH-Edu
cd SRH_Edu

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Initialize the database
python initial_data.py

# Start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd ../frontend/public

# Serve the frontend (using Python's built-in server)
python -m http.server 8080
```

### Accessing the Application
- Frontend: http://localhost:8080
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Admin Panel: http://localhost:8080/admin/login.html
  - Username: admin
  - Password: admin123

## Features

1. Educational Content
   - STI Information
   - Prevention Methods
   - Myth Busters

2. Interactive Tools
   - Symptom Checker
   - Knowledge Quiz
   - Clinic Locator

3. Admin Features
   - Content Management
   - Quiz Management
   - Clinic Information Updates

## Technologies Used

- Frontend:
  - HTML5
  - CSS3 (Tailwind CSS)
  - JavaScript
  - Font Awesome Icons

- Backend:
  - Python
  - FastAPI
  - SQLAlchemy
  - SQLite Database

## Project Structure
```
healthy-sex-healthy-life/
├── frontend/
│   └── public/
│       ├── admin/
│       ├── education/
│       ├── tools/
│       ├── resources/
│       ├── css/
│       └── js/
└── backend/
    ├── app/
    │   ├── routes/
    │   ├── models/
    │   └── config/
    ├── requirements.txt
    └── main.py
```

## Contributors
- Micah Buldo

## License
This project is licensed under the MIT License - see the LICENSE file for details
