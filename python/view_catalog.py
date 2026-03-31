import json
import os

def load_courses():
    """Load courses from the JSON file."""
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    courses_file = os.path.join(data_dir, 'courses.json')
    try:
        with open(courses_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: courses.json not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in courses.json.")
        return []

def format_time_slot(time_slot):
    """Format the time slot for display."""
    if time_slot:
        days = time_slot.get('days', '')
        start = time_slot.get('startTime', '')
        end = time_slot.get('endTime', '')
        return f"{days} {start}-{end}"
    return ""

def view_course_catalog():
    """Display the course catalog."""
    courses = load_courses()
    if not courses:
        print("No courses available.")
        return

    print("=" * 70)
    print("COURSE CATALOG")
    print("=" * 70)
    print(f"{'Code':<10} {'Title':<40} {'Credits':<8} {'Seats':<12} {'Time':<18} {'Prerequisites'}")
    print("-" * 70)

    for course in courses:
        code = course.get('code', '')
        title = course.get('title', '')
        credits = course.get('credits', 0)
        capacity = course.get('capacity', 0)
        time_str = format_time_slot(course.get('timeSlot'))
        prereqs = ', '.join(course.get('prerequisites', [])) or 'None'
        enrolled = len(course.get('enrolledStudents', []))
        seats = f"{enrolled}/{capacity}"

        print(f"{code:<10} {title:<40} {credits:<8} {seats:<12} {time_str:<18} {prereqs}")

if __name__ == "__main__":
    view_course_catalog()