# Healthy Sex, Healthy Life

An STI Awareness Web Application providing accurate, stigma-free information about sexual health.

## Description

This web application aims to educate users about STIs through:
- Educational content about STIs
- Interactive symptom checker
- Knowledge testing quiz
- Clinic locator for healthcare services in Nairobi
- Admin panel for content management

## Problem Statement

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

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for frontend development)
- Git

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/Mbuldo/Healthy-sex-healthy-life.git
cd Healthy-sex-healthy-life

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
- Your Name

## License
This project is licensed under the MIT License - see the LICENSE file for details
