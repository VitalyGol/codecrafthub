# CodeCraftHub API Test Guide

This guide provides comprehensive test cases for the Course Management API using curl commands. Copy and paste these commands into your terminal to test each endpoint.

**Prerequisites:**
- Flask app running on `http://localhost:5000`
- Run the app with: `python app.py`
- A tool to view formatted JSON (optional): `curl ... | json_pp` or `curl ... | python -m json.tool`

---

## 1. HEALTH CHECK ENDPOINT

### Test 1.1: Check API Status
```bash
curl -X GET http://localhost:5000/api/health
```

**Expected Response:**
```json
{
    "status": "OK",
    "message": "Course API is running"
}
```

---

## 2. CREATE COURSE - POST /api/courses

### Test 2.1: Create a Course (Success)
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "In Progress"
  }' | python -m json.tool
```

**Expected Response (Status: 201 Created):**
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

---

### Test 2.2: Create Another Course
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "JavaScript Essentials",
    "description": "Master JavaScript for web development",
    "target_date": "2026-11-15",
    "status": "Not Started"
  }' | python -m json.tool
```

**Expected Response (Status: 201 Created):**
```json
{
    "id": 2,
    "name": "JavaScript Essentials",
    "description": "Master JavaScript for web development",
    "target_date": "2026-11-15",
    "status": "Not Started",
    "created_at": "2026-06-14T10:35:20.654321"
}
```

---

### Test 2.3: Create One More Course
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Database Design",
    "description": "Learn SQL and database design patterns",
    "target_date": "2026-10-20",
    "status": "Completed"
  }' | python -m json.tool
```

**Expected Response (Status: 201 Created):**
```json
{
    "id": 3,
    "name": "Database Design",
    "description": "Learn SQL and database design patterns",
    "target_date": "2026-10-20",
    "status": "Completed",
    "created_at": "2026-06-14T10:40:15.987654"
}
```

---

## 3. ERROR TESTS - POST /api/courses

### Test 3.1: Missing Required Field (name)
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Missing name field",
    "target_date": "2026-12-31",
    "status": "Not Started"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Missing required field: name"
}
```

---

### Test 3.2: Missing Required Field (description)
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Incomplete Course",
    "target_date": "2026-12-31",
    "status": "Not Started"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Missing required field: description"
}
```

---

### Test 3.3: Missing Required Field (target_date)
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Missing Date Course",
    "description": "This course has no target date",
    "status": "Not Started"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Missing required field: target_date"
}
```

---

### Test 3.4: Missing Required Field (status)
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Missing Status Course",
    "description": "This course has no status",
    "target_date": "2026-12-31"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Missing required field: status"
}
```

---

### Test 3.5: Invalid Status Value
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Invalid Status Course",
    "description": "Course with invalid status",
    "target_date": "2026-12-31",
    "status": "Invalid"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

---

### Test 3.6: Invalid Date Format
```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bad Date Course",
    "description": "Course with invalid date format",
    "target_date": "12/31/2026",
    "status": "Not Started"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Invalid date format. Use YYYY-MM-DD"
}
```

---

## 4. GET ALL COURSES - GET /api/courses

### Test 4.1: Retrieve All Courses
```bash
curl -X GET http://localhost:5000/api/courses | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "total": 3,
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
        },
        {
            "id": 3,
            "name": "Database Design",
            "description": "Learn SQL and database design patterns",
            "target_date": "2026-10-20",
            "status": "Completed",
            "created_at": "2026-06-14T10:40:15.987654"
        }
    ]
}
```

---

## 5. GET SPECIFIC COURSE - GET /api/courses/<id>

### Test 5.1: Get Course with ID 1 (Success)
```bash
curl -X GET http://localhost:5000/api/courses/1 | python -m json.tool
```

**Expected Response (Status: 200 OK):**
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

---

### Test 5.2: Get Course with ID 2 (Success)
```bash
curl -X GET http://localhost:5000/api/courses/2 | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "id": 2,
    "name": "JavaScript Essentials",
    "description": "Master JavaScript for web development",
    "target_date": "2026-11-15",
    "status": "Not Started",
    "created_at": "2026-06-14T10:35:20.654321"
}
```

---

### Test 5.3: Get Course with ID 3 (Success)
```bash
curl -X GET http://localhost:5000/api/courses/3 | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "id": 3,
    "name": "Database Design",
    "description": "Learn SQL and database design patterns",
    "target_date": "2026-10-20",
    "status": "Completed",
    "created_at": "2026-06-14T10:40:15.987654"
}
```

---

### Test 5.4: Get Non-existent Course (Error)
```bash
curl -X GET http://localhost:5000/api/courses/999 | python -m json.tool
```

**Expected Response (Status: 404 Not Found):**
```json
{
    "error": "Course with id 999 not found"
}
```

---

## 6. UPDATE COURSE - PUT /api/courses/<id>

### Test 6.1: Update Course Name Only
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Advanced Python"
  }' | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "id": 1,
    "name": "Advanced Python",
    "description": "Learn Python programming fundamentals",
    "target_date": "2026-12-31",
    "status": "In Progress",
    "created_at": "2026-06-14T10:30:45.123456"
}
```

---

### Test 6.2: Update Course Status
```bash
curl -X PUT http://localhost:5000/api/courses/2 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }' | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "id": 2,
    "name": "JavaScript Essentials",
    "description": "Master JavaScript for web development",
    "target_date": "2026-11-15",
    "status": "In Progress",
    "created_at": "2026-06-14T10:35:20.654321"
}
```

---

### Test 6.3: Update Multiple Fields
```bash
curl -X PUT http://localhost:5000/api/courses/3 \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Learn SQL, NoSQL, and advanced database design patterns",
    "target_date": "2026-09-15",
    "status": "In Progress"
  }' | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "id": 3,
    "name": "Database Design",
    "description": "Learn SQL, NoSQL, and advanced database design patterns",
    "target_date": "2026-09-15",
    "status": "In Progress",
    "created_at": "2026-06-14T10:40:15.987654"
}
```

---

## 7. ERROR TESTS - PUT /api/courses/<id>

### Test 7.1: Update Non-existent Course
```bash
curl -X PUT http://localhost:5000/api/courses/999 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Non-existent Course"
  }' | python -m json.tool
```

**Expected Response (Status: 404 Not Found):**
```json
{
    "error": "Course with id 999 not found"
}
```

---

### Test 7.2: Update with Invalid Status
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "On Hold"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Invalid status. Must be one of: Not Started, In Progress, Completed"
}
```

---

### Test 7.3: Update with Invalid Date Format
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "target_date": "31-12-2026"
  }' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Invalid date format. Use YYYY-MM-DD"
}
```

---

### Test 7.4: Update with Empty Body
```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{}' | python -m json.tool
```

**Expected Response (Status: 400 Bad Request):**
```json
{
    "error": "Request body cannot be empty"
}
```

---

## 8. DELETE COURSE - DELETE /api/courses/<id>

### Test 8.1: Delete a Course (Success)
```bash
curl -X DELETE http://localhost:5000/api/courses/1 | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "message": "Course with id 1 deleted successfully",
    "deleted_course": {
        "id": 1,
        "name": "Advanced Python",
        "description": "Learn Python programming fundamentals",
        "target_date": "2026-12-31",
        "status": "In Progress",
        "created_at": "2026-06-14T10:30:45.123456"
    }
}
```

---

### Test 8.2: Delete Another Course
```bash
curl -X DELETE http://localhost:5000/api/courses/2 | python -m json.tool
```

**Expected Response (Status: 200 OK):**
```json
{
    "message": "Course with id 2 deleted successfully",
    "deleted_course": {
        "id": 2,
        "name": "JavaScript Essentials",
        "description": "Master JavaScript for web development",
        "target_date": "2026-11-15",
        "status": "In Progress",
        "created_at": "2026-06-14T10:35:20.654321"
    }
}
```

---

### Test 8.3: Delete Non-existent Course (Error)
```bash
curl -X DELETE http://localhost:5000/api/courses/999 | python -m json.tool
```

**Expected Response (Status: 404 Not Found):**
```json
{
    "error": "Course with id 999 not found"
}
```

---

## 9. ADVANCED TEST SCENARIOS

### Scenario 1: Create Multiple Courses and Verify Counts
```bash
# Check initial count
curl -X GET http://localhost:5000/api/courses | python -m json.tool

# Create a new course
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Web Development",
    "description": "Learn HTML, CSS, and JavaScript",
    "target_date": "2026-08-30",
    "status": "Not Started"
  }'

# Check count again - should be increased by 1
curl -X GET http://localhost:5000/api/courses | python -m json.tool
```

---

### Scenario 2: Full Course Lifecycle
```bash
# 1. Create a course
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Skill",
    "description": "Learn something new",
    "target_date": "2026-12-01",
    "status": "Not Started"
  }' | python -m json.tool

# 2. Update status to In Progress
curl -X PUT http://localhost:5000/api/courses/COURSE_ID \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }' | python -m json.tool

# 3. View the updated course
curl -X GET http://localhost:5000/api/courses/COURSE_ID | python -m json.tool

# 4. Update status to Completed
curl -X PUT http://localhost:5000/api/courses/COURSE_ID \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Completed"
  }' | python -m json.tool

# 5. Delete the course
curl -X DELETE http://localhost:5000/api/courses/COURSE_ID | python -m json.tool
```
*(Note: Replace COURSE_ID with the actual ID returned from the create request)*

---

## 10. TIPS FOR TESTING

1. **Format JSON Output Nicely**
   - Use `| python -m json.tool` at the end of curl commands
   - Or use `| jq` if you have jq installed

2. **Save Response to File**
   ```bash
   curl -X GET http://localhost:5000/api/courses > response.json
   ```

3. **Use Verbose Mode to See Headers**
   ```bash
   curl -v -X GET http://localhost:5000/api/courses
   ```

4. **Check HTTP Status Code Only**
   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:5000/api/courses
   ```

5. **View Response Headers**
   ```bash
   curl -i -X GET http://localhost:5000/api/courses
   ```

6. **Test with Postman**
   - Import these curl commands into Postman
   - Or create a new collection with these requests
   - Use environment variables for the base URL

---

## Summary of Status Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Successful GET, PUT, DELETE |
| 201 | Created | Successful POST |
| 400 | Bad Request | Missing/invalid fields, bad data |
| 404 | Not Found | Course doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method for endpoint |
| 500 | Server Error | Unexpected server error |

---

## Valid Status Values

The `status` field must be exactly one of these three values:
- `"Not Started"`
- `"In Progress"`
- `"Completed"`

---

## Date Format

The `target_date` field must be in `YYYY-MM-DD` format:
- ✅ Valid: `"2026-12-31"`, `"2026-01-15"`, `"2026-06-14"`
- ❌ Invalid: `"12/31/2026"`, `"31-12-2026"`, `"2026/12/31"`
