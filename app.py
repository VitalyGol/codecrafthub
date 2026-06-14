# Flask REST API for Course Management
# This application provides CRUD operations for managing courses with JSON storage
# Each course has: id, name, description, target_date, status, and created_at

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration: path to the JSON file where courses will be stored
COURSES_FILE = 'courses.json'


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_courses():
    """
    Load courses from the JSON file.
    If the file doesn't exist, create an empty one.
    
    Returns:
        dict: A dictionary containing the courses list and next_id
    """
    if not os.path.exists(COURSES_FILE):
        # Create a new JSON file with empty courses list and next_id starting at 1
        initial_data = {
            'courses': [],
            'next_id': 1
        }
        save_courses(initial_data)
        return initial_data
    
    try:
        with open(COURSES_FILE, 'r') as file:
            data = json.load(file)
            return data
    except (json.JSONDecodeError, IOError) as e:
        # Handle file read errors
        print(f"Error reading courses file: {e}")
        return {'courses': [], 'next_id': 1}


def save_courses(data):
    """
    Save courses to the JSON file.
    
    Args:
        data (dict): Dictionary containing 'courses' list and 'next_id'
    """
    try:
        with open(COURSES_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing courses file: {e}")
        raise


def validate_course_data(data):
    """
    Validate that required fields are present and have valid values.
    
    Args:
        data (dict): Course data to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check if required fields are present
    required_fields = ['name', 'description', 'target_date', 'status']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"
    
    # Validate status values
    valid_statuses = ['Not Started', 'In Progress', 'Completed']
    if data['status'] not in valid_statuses:
        return False, f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
    
    # Validate date format (YYYY-MM-DD)
    try:
        datetime.strptime(data['target_date'], '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"
    
    return True, None


def course_exists(course_id, courses):
    """
    Check if a course with the given ID exists.
    
    Args:
        course_id (int): ID of the course to check
        courses (list): List of courses
        
    Returns:
        int: Index of the course if found, -1 otherwise
    """
    for index, course in enumerate(courses):
        if course['id'] == course_id:
            return index
    return -1


# ============================================================================
# CRUD ENDPOINTS
# ============================================================================

@app.route('/api/courses', methods=['POST'])
def create_course():
    """
    Create a new course.
    
    Request body should contain:
        - name (string, required)
        - description (string, required)
        - target_date (string, required, format: YYYY-MM-DD)
        - status (string, required, options: "Not Started", "In Progress", "Completed")
    
    Returns:
        JSON response with the created course or error message
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate the input data
        is_valid, error_message = validate_course_data(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        # Load existing courses
        courses_data = load_courses()
        courses = courses_data['courses']
        
        # Create new course object with auto-generated id and timestamp
        new_course = {
            'id': courses_data['next_id'],
            'name': data['name'],
            'description': data['description'],
            'target_date': data['target_date'],
            'status': data['status'],
            'created_at': datetime.now().isoformat()
        }
        
        # Add the new course to the list
        courses.append(new_course)
        
        # Update next_id for the next course
        courses_data['next_id'] += 1
        
        # Save updated courses to file
        save_courses(courses_data)
        
        # Return the created course with 201 Created status code
        return jsonify(new_course), 201
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    """
    Retrieve all courses.
    
    Returns:
        JSON response with list of all courses
    """
    try:
        # Load courses from file
        courses_data = load_courses()
        courses = courses_data['courses']
        
        # Return all courses with 200 OK status code
        return jsonify({
            'total': len(courses),
            'courses': courses
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve a specific course by ID.
    
    Args:
        course_id (int): ID of the course to retrieve
    
    Returns:
        JSON response with the course or error message
    """
    try:
        # Load courses from file
        courses_data = load_courses()
        courses = courses_data['courses']
        
        # Find the course with matching ID
        index = course_exists(course_id, courses)
        
        if index == -1:
            # Course not found
            return jsonify({'error': f'Course with id {course_id} not found'}), 404
        
        # Return the found course
        return jsonify(courses[index]), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update an existing course.
    
    Args:
        course_id (int): ID of the course to update
    
    Request body should contain one or more of:
        - name (string)
        - description (string)
        - target_date (string, format: YYYY-MM-DD)
        - status (string, options: "Not Started", "In Progress", "Completed")
    
    Returns:
        JSON response with the updated course or error message
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body cannot be empty'}), 400
        
        # Load courses from file
        courses_data = load_courses()
        courses = courses_data['courses']
        
        # Find the course with matching ID
        index = course_exists(course_id, courses)
        
        if index == -1:
            # Course not found
            return jsonify({'error': f'Course with id {course_id} not found'}), 404
        
        # Validate the new data (only validate fields that are being updated)
        if 'status' in data and data['status']:
            valid_statuses = ['Not Started', 'In Progress', 'Completed']
            if data['status'] not in valid_statuses:
                return jsonify({'error': f'Invalid status. Must be one of: {", ".join(valid_statuses)}'}), 400
        
        if 'target_date' in data and data['target_date']:
            try:
                datetime.strptime(data['target_date'], '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
        
        # Update only the fields that were provided
        if 'name' in data and data['name']:
            courses[index]['name'] = data['name']
        if 'description' in data and data['description']:
            courses[index]['description'] = data['description']
        if 'target_date' in data and data['target_date']:
            courses[index]['target_date'] = data['target_date']
        if 'status' in data and data['status']:
            courses[index]['status'] = data['status']
        
        # Save updated courses to file
        save_courses(courses_data)
        
        # Return the updated course
        return jsonify(courses[index]), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Delete a course by ID.
    
    Args:
        course_id (int): ID of the course to delete
    
    Returns:
        JSON response confirming deletion or error message
    """
    try:
        # Load courses from file
        courses_data = load_courses()
        courses = courses_data['courses']
        
        # Find the course with matching ID
        index = course_exists(course_id, courses)
        
        if index == -1:
            # Course not found
            return jsonify({'error': f'Course with id {course_id} not found'}), 404
        
        # Remove the course from the list
        deleted_course = courses.pop(index)
        
        # Save updated courses to file
        save_courses(courses_data)
        
        # Return confirmation message
        return jsonify({
            'message': f'Course with id {course_id} deleted successfully',
            'deleted_course': deleted_course
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


# ============================================================================
# UTILITY ENDPOINTS
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        JSON response indicating API status
    """
    return jsonify({'status': 'OK', 'message': 'Course API is running'}), 200


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 Method Not Allowed errors"""
    return jsonify({'error': 'Method not allowed'}), 405


@app.errorhandler(400)
def bad_request(error):
    """Handle 400 Bad Request errors"""
    return jsonify({'error': 'Bad request'}), 400


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    # Run the Flask application
    # Set debug=True for development (auto-reload on file changes)
    # Set host='0.0.0.0' to allow external connections
    # Set port=5000 (default Flask port)
    app.run(debug=True, host='0.0.0.0', port=5000)
