# CodeCraftHub - Course Management REST API

A beginner-friendly REST API built with Flask for managing courses. Learn how to build CRUD operations, handle JSON data, and work with REST APIs through this practical project.

![Status](https://img.shields.io/badge/status-ready-brightgreen)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/flask-latest-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Learning Resources](#learning-resources)

---

## 🎯 Project Overview

**CodeCraftHub** is a course management system that demonstrates fundamental concepts of building REST APIs. It allows you to create, read, update, and delete course information stored in a JSON file.

This project is perfect for:
- Beginners learning REST API concepts
- Students studying Flask framework
- Anyone new to CRUD operations
- Developers learning how to work with JSON data

### What You'll Learn

By exploring this project, you'll understand:
- ✅ How to create REST API endpoints
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ JSON file handling in Python
- ✅ Error handling and validation
- ✅ HTTP status codes and methods
- ✅ Request/Response patterns
- ✅ Best practices for API design

---

## ✨ Features

### Core Features
- **Create Courses** - Add new courses with all required information
- **Read Courses** - Retrieve all courses or a specific course by ID
- **Update Courses** - Modify course details (name, description, status, target date)
- **Delete Courses** - Remove courses from the system
- **Auto-generated IDs** - Courses receive unique IDs automatically (starting from 1)
- **Timestamps** - Track when each course was created

### Data Validation
- ✅ Required field validation (name, description, target_date, status)
- ✅ Valid status values enforcement ("Not Started", "In Progress", "Completed")
- ✅ Date format validation (YYYY-MM-DD)
- ✅ Proper HTTP error responses

### JSON Storage
- ✅ Persistent data storage in `courses.json`
- ✅ Automatic file creation if not exists
- ✅ Formatted JSON for easy reading
- ✅ Maintains course counter for auto-incrementing IDs

### Error Handling
- ✅ Missing required fields detection
- ✅ Invalid data validation
- ✅ Course not found errors
- ✅ File I/O error handling
- ✅ User-friendly error messages

---

## 💻 Installation

### Step 1: Check Python Installation

First, make sure Python 3.7 or higher is installed on your system.

```bash
python --version
```

You should see output like: `Python 3.9.0` or higher.

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

---

### Step 2: Create a Project Directory

Navigate to where you want to store the project and create a folder:

```bash
cd ~/Documents
mkdir codecrafthub
cd codecrafthub
```

---

### Step 3: Create a Virtual Environment

A virtual environment is an isolated Python workspace. This is a best practice for Python projects.

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

After activation, your terminal should show `(venv)` at the beginning of each line.

---

### Step 4: Install Flask

With the virtual environment activated, install Flask:

```bash
pip install flask
```

You'll see output showing the installation progress. Flask and its dependencies will be installed.

---

### Step 5: Add Project Files

You should have these files in your project directory:

1. **app.py** - The main Flask application
2. **courses.json** - Data storage file (auto-created by app if missing)
3. **API_TESTS.md** - Test cases and examples
4. **README.md** - This file

Your project structure should look like:
```
codecrafthub/
├── venv/                 (virtual environment folder)
├── app.py               (main application)
├── courses.json         (data file)
├── API_TESTS.md         (test guide)
└── README.md            (this file)
```

---

## 🚀 Running the Application

### Step 1: Activate Virtual Environment

Before running the app, make sure your virtual environment is activated:

```bash
# macOS/Linux:
source venv/bin/activate

# Windows:
# venv\Scripts\activate
```

### Step 2: Run the Flask App

```bash
python app.py
```

### Step 3: Look for This Output

You should see something like:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

**Congratulations!** Your API is now running on `http://localhost:5000`

### Step 4: Verify the API is Working

Open a new terminal (keep the Flask app running) and run:

```bash
curl http://localhost:5000/api/health
```

You should see: `{"status":"OK","message":"Course API is running"}`

### Step 5: Stop the Application

Press `CTRL+C` in the terminal where Flask is running to stop the server.

---

## 📡 API Endpoints

This section explains all available endpoints. Each endpoint uses HTTP methods to perform different operations.

### Understanding HTTP Methods

- **GET** - Retrieve data (don't modify anything)
- **POST** - Create new data
- **PUT** - Update existing data
- **DELETE** - Remove data

---

### 1. Health Check Endpoint

Check if the API is running and healthy.

**Endpoint:** `GET /api/health`

**Description:** Returns the status of the API.

**Example Request:**
```bash
curl http://localhost:5000/api/health
```

**Example Response (Status: 200 OK):**
```json
{
    "status": "OK",
    "message": "Course API is running"
}
```

---

### 2. Create a Course

Add a new course to the system.

**Endpoint:** `POST /api/courses`

**Required Fields:**
- `name` (string) - Course name
- `description` (string) - Course description
- `target_date` (string) - Target completion date in YYYY-MM-DD format
- `status` (string) - Course status: "Not Started", "In Progress", or "Completed"

**Auto-generated Fields:**
- `id` - Unique identifier (starts from 1)
- `created_at` - Timestamp when course was created

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "In Progress"
  }'
```

**Example Response (Status: 201 Created):**
```json
{
    "id": 1,
    "name": "Python Basics",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "In Progress",
    "created_at": "2026-06-14T10:30:45.123456"
}
```

**Common Errors:**

Missing required field:
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name": "Incomplete Course", "description": "Missing fields"}'
```
Response (Status: 400 Bad Request):
```json
{"error": "Missing required field: target_date"}
```

Invalid status:
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Course",
    "description": "Test",
    "target_date": "2026-12-31",
    "status": "Invalid"
  }'
```
Response (Status: 400 Bad Request):
```json
{"error": "Invalid status. Must be one of: Not Started, In Progress, Completed"}
```

---

### 3. Get All Courses

Retrieve a list of all courses in the system.

**Endpoint:** `GET /api/courses`

**Description:** Returns all courses with total count.

**Example Request:**
```bash
curl http://localhost:5000/api/courses
```

**Example Response (Status: 200 OK):**
```json
{
    "total": 2,
    "courses": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python programming fundamentals",
            "target_date": "2026-12-31",
            "status": "In Progress",
            "created_at": "2026-06-14T10:30:45.123456"
        },
        {
            "id": 2,
            "name": "JavaScript Essentials",
            "description": "Master JavaScript for web development",
            "target_date": "2026-11-15",
            "status": "Not Started",
            "created_at": "2026-06-14T10:35:20.654321"
        }
    ]
}
```

---

### 4. Get a Specific Course

Retrieve a single course by its ID.

**Endpoint:** `GET /api/courses/<id>`

**URL Parameters:**
- `id` (integer) - The course ID

**Example Request (get course with ID 1):**
```bash
curl http://localhost:5000/api/courses/1
```

**Example Response (Status: 200 OK):**
```json
{
    "id": 1,
    "name": "Python Basics",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "In Progress",
    "created_at": "2026-06-14T10:30:45.123456"
}
```

**Error Response (Status: 404 Not Found):**
```bash
curl http://localhost:5000/api/courses/999
```
```json
{"error": "Course with id 999 not found"}
```

---

### 5. Update a Course

Modify an existing course. You can update one field or multiple fields at once.

**Endpoint:** `PUT /api/courses/<id>`

**URL Parameters:**
- `id` (integer) - The course ID

**Optional Fields** (send only the fields you want to update):
- `name` (string)
- `description` (string)
- `target_date` (string, format: YYYY-MM-DD)
- `status` (string)

**Example Request (update status only):**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Completed"
  }'
```

**Example Response (Status: 200 OK):**
```json
{
    "id": 1,
    "name": "Python Basics",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "Completed",
    "created_at": "2026-06-14T10:30:45.123456"
}
```

**Example Request (update multiple fields):**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Advanced Python programming techniques",
    "target_date": "2027-01-15",
    "status": "In Progress"
  }'
```

**Error Response - Course not found (Status: 404):**
```bash
curl -X PUT http://localhost:5000/api/courses/999 \
  -H "Content-Type: application/json" \
  -d '{"status": "Completed"}'
```
```json
{"error": "Course with id 999 not found"}
```

---

### 6. Delete a Course

Remove a course from the system.

**Endpoint:** `DELETE /api/courses/<id>`

**URL Parameters:**
- `id` (integer) - The course ID

**Example Request (delete course with ID 1):**
```bash
curl -X DELETE http://localhost:5000/api/courses/1
```

**Example Response (Status: 200 OK):**
```json
{
    "message": "Course with id 1 deleted successfully",
    "deleted_course": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python programming fundamentals",
        "target_date": "2026-12-31",
        "status": "Completed",
        "created_at": "2026-06-14T10:30:45.123456"
    }
}
```

**Error Response - Course not found (Status: 404):**
```bash
curl -X DELETE http://localhost:5000/api/courses/999
```
```json
{"error": "Course with id 999 not found"}
```

---

## 🧪 Testing

### Using curl (Command Line)

The easiest way to test the API is using `curl`, which comes pre-installed on most systems.

**Basic curl syntax:**
```bash
curl -X METHOD http://localhost:5000/endpoint
```

**Test 1: Create a course**
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "In Progress"
  }'
```

**Test 2: Get all courses**
```bash
curl http://localhost:5000/api/courses
```

**Test 3: Get specific course**
```bash
curl http://localhost:5000/api/courses/1
```

**Test 4: Update a course**
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "Completed"}'
```

**Test 5: Delete a course**
```bash
curl -X DELETE http://localhost:5000/api/courses/1
```

### Pretty-print JSON Responses

Add `| python -m json.tool` to format JSON output:

```bash
curl http://localhost:5000/api/courses | python -m json.tool
```

### Using Postman (GUI Tool)

For a graphical interface, you can use Postman:

1. Download Postman from [postman.com](https://www.postman.com/downloads/)
2. Create a new request
3. Select the HTTP method (GET, POST, PUT, DELETE)
4. Enter the URL: `http://localhost:5000/api/courses`
5. For POST/PUT: Add JSON in the Body tab
6. Click "Send"

### Running Test Suite

A comprehensive test file is included: **API_TESTS.md**

This file contains:
- 30+ test cases
- Success scenarios
- Error scenarios
- Examples of valid/invalid data
- Advanced testing scenarios

To run tests:
1. Make sure the Flask app is running
2. Open **API_TESTS.md**
3. Copy any curl command and paste it in your terminal
4. Compare the response with the expected result

---

## 🔧 Troubleshooting

### Problem 1: "Command 'python' not found"

**Solution:**
- Try `python3` instead: `python3 --version`
- Or check your Python installation: Windows might require `py -m pip install flask`

### Problem 2: "Flask module not found"

**Error message:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
1. Make sure your virtual environment is activated (you should see `(venv)` in terminal)
2. Install Flask again:
   ```bash
   pip install flask
   ```
3. Verify installation:
   ```bash
   python -c "import flask; print(flask.__version__)"
   ```

### Problem 3: "Address already in use" or "Port 5000 in use"

**Error message:** `OSError: [Errno 48] Address already in use`

**Solution:**

Option A: Stop other Flask apps running on port 5000
```bash
# Find what's using port 5000 (macOS/Linux)
lsof -i :5000

# Kill the process
kill -9 <PID>
```

Option B: Use a different port by editing app.py
- Change the last line: `app.run(debug=True, host='0.0.0.0', port=5001)`

### Problem 4: "Connection refused" when testing

**Error message:** `Connection refused` or `curl: (7) Failed to connect`

**Solution:**
1. Make sure Flask app is running in another terminal
2. Make sure the app started successfully (look for `Running on http://0.0.0.0:5000`)
3. Use `http://localhost:5000` instead of `http://127.0.0.1:5000` if issues persist

### Problem 5: "courses.json not found" error

**Solution:**
The file is created automatically on first request. If it's not created:
1. Make sure the Flask app has write permissions in its directory
2. Manually create it:
   ```bash
   echo '{"courses": [], "next_id": 1}' > courses.json
   ```

### Problem 6: "Invalid date format" error

**Solution:**
Date must be in `YYYY-MM-DD` format. Examples:
- ✅ Valid: `"2026-12-31"`, `"2026-01-15"`
- ❌ Invalid: `"12/31/2026"`, `"2026/12/31"`, `"Dec 31, 2026"`

### Problem 7: "Invalid status" error

**Solution:**
Status must be exactly one of these three values:
- ✅ `"Not Started"`
- ✅ `"In Progress"`
- ✅ `"Completed"`

❌ Invalid: `"NotStarted"`, `"In progress"`, `"Done"`, `"On Hold"`

---

## 📁 Project Structure

Understanding the project layout helps you know what each file does:

```
codecrafthub/
│
├── app.py                          # Main Flask application
│   ├── Imports and setup
│   ├── Helper functions (load/save/validate)
│   ├── CRUD endpoints (POST, GET, PUT, DELETE)
│   ├── Error handlers
│   └── Main entry point
│
├── courses.json                    # Data storage (auto-created)
│   ├── "courses": []              # List of all courses
│   └── "next_id": 1               # Counter for auto-incrementing IDs
│
├── API_TESTS.md                    # Test cases and examples
│   ├── 10 test sections
│   ├── 30+ curl examples
│   ├── Success scenarios
│   ├── Error scenarios
│   └── Advanced test examples
│
└── README.md                       # This file
    ├── Project overview
    ├── Installation guide
    ├── API documentation
    ├── Testing guide
    └── Troubleshooting
```

### Key Files Explained

#### app.py (Main Application)

**Imports Section** (Lines 1-8)
- Imports Flask, request, jsonify, json, os, datetime
- These are libraries that help build the API

**Configuration** (Lines 13-14)
- Sets the path to `courses.json` file

**Helper Functions** (Lines 18-127)
- `load_courses()` - Reads data from courses.json
- `save_courses()` - Writes data to courses.json
- `validate_course_data()` - Checks if data is valid
- `course_exists()` - Searches for a course by ID

**Endpoints** (Lines 131-308)
- 6 main endpoints:
  - POST /api/courses - Create
  - GET /api/courses - Read all
  - GET /api/courses/<id> - Read one
  - PUT /api/courses/<id> - Update
  - DELETE /api/courses/<id> - Delete
  - GET /api/health - Health check

**Error Handlers** (Lines 311-328)
- Handles 404, 405, 400 errors

**Entry Point** (Lines 331-341)
- Starts the Flask development server

#### courses.json (Data File)

Initial structure:
```json
{
    "courses": [],
    "next_id": 1
}
```

After adding a course:
```json
{
    "courses": [
        {
            "id": 1,
            "name": "Python Basics",
            "description": "Learn Python programming",
            "target_date": "2026-12-31",
            "status": "In Progress",
            "created_at": "2026-06-14T10:30:45.123456"
        }
    ],
    "next_id": 2
}
```

---

## 📖 Learning Resources

### Understanding REST APIs

**What is REST?**
REST (Representational State Transfer) is an architectural style for building APIs. It uses:
- **Resources** (courses) represented by URLs
- **HTTP Methods** (GET, POST, PUT, DELETE) to perform actions
- **Status Codes** to indicate success/failure

**Key Concepts:**
- GET requests retrieve data without modification
- POST requests create new data
- PUT requests update existing data
- DELETE requests remove data

### Python and Flask Concepts

**Helpful Python knowledge:**
- JSON format and `json` module
- Dictionaries and lists
- String formatting
- File I/O operations
- Error handling (try/except)

**Flask-specific:**
- Route decorators (`@app.route()`)
- Request handling
- JSON responses
- Error handlers

### Recommended Reading

1. **Flask Official Documentation**
   - https://flask.palletsprojects.com/

2. **REST API Design Guide**
   - https://restfulapi.net/

3. **HTTP Status Codes**
   - https://httpwg.org/specs/rfc7231.html#status.codes

4. **JSON Tutorial**
   - https://www.json.org/

### Next Steps for Learning

1. **Enhance the API:**
   - Add search/filtering functionality
   - Add sorting options
   - Add pagination for large datasets

2. **Add Database:**
   - Replace JSON with SQLite
   - Use SQLAlchemy ORM
   - Learn about database relationships

3. **Add Authentication:**
   - Implement user login
   - Add JWT tokens
   - Protect endpoints with authentication

4. **Improve Error Handling:**
   - Custom exception classes
   - Logging system
   - Detailed error messages

5. **Deploy the API:**
   - Deploy to Heroku, AWS, or Google Cloud
   - Set up CI/CD pipeline
   - Monitor API performance

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

This is a beginner learning project. Feel free to:
- Modify the code to understand how it works
- Add new features
- Experiment with different data structures
- Create your own courses or endpoints

---

## 💡 Tips for Success

1. **Start simple** - Create, then read, then update, then delete
2. **Use the test guide** - API_TESTS.md has working examples
3. **Read error messages** - They tell you what's wrong
4. **Experiment** - Try modifying the code and see what happens
5. **Ask questions** - Learning is an iterative process
6. **Practice** - Build similar APIs with different resources

---

## 📞 Questions?

If you encounter issues:
1. Check the **Troubleshooting** section above
2. Review the **API Endpoints** section
3. Look at **API_TESTS.md** for working examples
4. Check Flask error messages in your terminal

---

**Happy Learning! 🚀**

Remember: Every expert was once a beginner. Keep practicing and exploring!
