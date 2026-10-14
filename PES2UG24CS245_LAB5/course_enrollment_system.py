
"""Course enrollment system with safer operations and improved code quality."""

import hashlib
import os
import secrets

courses = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

total_tuition = 0.0


def enrollStudent(course_id, student_name, credits_registered=3,
                  audit_trail=None):
    """Enroll a student if the requested course has available seats."""
    global total_tuition

    if audit_trail is None:
        audit_trail = []

    if course_id not in courses:
        return False

    course = courses[course_id]

    if course["is_closed"] or course["seats"] <= 0:
        return False

    if not student_name.strip() or credits_registered <= 0:
        return False

    course["seats"] -= 1
    if course["seats"] == 0:
        course["is_closed"] = True

    total_tuition += course["fee"]

    audit_trail.append(
        f"Enrolled student {student_name} in course "
        f"{course_id} with {credits_registered} credits successfully"
    )
    return True


def dropCourse(course_id):
    """Restore a seat when a valid course enrollment is dropped."""
    course = courses.get(course_id)

    if course is None:
        return False

    course["seats"] += 1
    course["is_closed"] = False
    return True


def checkCourseStatus(course_id):
    """Return whether a course exists and is open."""
    course = courses.get(course_id)

    if course is None:
        return False

    return not course["is_closed"] and course["seats"] > 0


def calculateScholarshipTuition(course_id, discount_rate):
    """Calculate tuition after a discount percentage from 0 to 100."""
    if course_id not in courses:
        raise ValueError(f"Unknown course ID: {course_id}")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be a number.")

    if not 0 <= discount_rate <= 100:
        raise ValueError("Discount rate must be between 0 and 100.")

    base_fee = courses[course_id]["fee"]
    return round(base_fee * (1 - discount_rate / 100), 2)


def generateStudentHash(roll_no):
    """Generate a SHA-256 hash of a student roll number."""
    return hashlib.sha256(roll_no.encode("utf-8")).hexdigest()


def generateEnrollmentOtp():
    """Generate a four-digit security-conscious OTP."""
    return f"{secrets.randbelow(9000) + 1000}"


def exportCourseRoster(filename="course_roster.txt"):
    """Write course details to a roster file."""
    with open(filename, "w", encoding="utf-8") as roster_file:
        for course_id, details in courses.items():
            roster_file.write(
                f"{course_id}: {details['title']}, "
                f"Seats: {details['seats']}, "
                f"Fee: {details['fee']:.2f}, "
                f"Closed: {details['is_closed']}\n"
            )

    print(f"Course roster exported to: {os.path.abspath(filename)}")


def getOpenCoursesSummary(course_catalog):
    """Return the number of courses that are open and have seats."""
    return sum(
        1
        for details in course_catalog.values()
        if not details["is_closed"] and details["seats"] > 0
    )


def main():
    """Run example course enrollment operations."""
    audit_trail = []

    enrolled = enrollStudent(
        "CS101", "Kritika", 4, audit_trail
    )
    print("Enrollment successful:", enrolled)

    dropped = dropCourse("CS101")
    print("Course dropped:", dropped)

    print("Is CS101 open:", checkCourseStatus("CS101"))
    print(
        "Scholarship Fee:",
        calculateScholarshipTuition("CS303", 25),
    )
    print("Student Hash:", generateStudentHash("REG_2026_091"))
    print("Enrollment OTP:", generateEnrollmentOtp())

    exportCourseRoster()
    print("Open courses:", getOpenCoursesSummary(courses))
    print("Audit trail:", audit_trail)


if __name__ == "__main__":
    main()
