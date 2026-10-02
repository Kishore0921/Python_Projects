import json
import os

class Student:
    """Class representing an individual student."""
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        """Convert student object to a dictionary."""
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

class StudentManager:
    """Class managing student operations, file handling, and exceptions."""
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_from_file()

    def load_from_file(self):
        """Load student records from a JSON file using file and exception handling."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.students = {k: Student(**v) for k, v in data.items()}
            except (json.JSONDecodeError, IOError):
                print("Error reading file. Starting with an empty database.")
                self.students = {}

    def save_to_file(self):
        """Save student records to a JSON file."""
        try:
            data = {k: v.to_dict() for k, v in self.students.items()}
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
        except IOError:
            print("Error: Could not save data to file.")

    def add_student(self):
        """Add a new student record."""
        print("\n--- Add Student ---")
        roll_no = input("Enter Roll Number: ").strip()
        if not roll_no:
            print("Roll number cannot be empty.")
            return
        if roll_no in self.students:
            print("Student with this Roll Number already exists!")
            return

        name = input("Enter Name: ").strip()
        
        # Exception handling for integer inputs (Age)
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Invalid input! Age must be a number.")
            return

        grade = input("Enter Grade: ").strip()
        
        # Store using OOP and Dictionaries
        self.students[roll_no] = Student(roll_no, name, age, grade)
        self.save_to_file()
        print("Student added successfully!")

    def view_students(self):
        """View all student records stored in the list/dictionary."""
        print("\n--- All Students ---")
        if not self.students:
            print("No student records found.")
            return
        for roll_no, student in self.students.items():
            print(f"Roll No: {roll_no} | Name: {student.name} | Age: {student.age} | Grade: {student.grade}")

    def search_student(self):
        """Search for a specific student by Roll Number."""
        print("\n--- Search Student ---")
        roll_no = input("Enter Roll Number to search: ").strip()
        student = self.students.get(roll_no)
        if student:
            print(f"Found -> Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
        else:
            print("Student not found.")

    def update_student(self):
        """Update an existing student record."""
        print("\n--- Update Student ---")
        roll_no = input("Enter Roll Number to update: ").strip()
        if roll_no not in self.students:
            print("Student not found.")
            return

        student = self.students[roll_no]
        print(f"Updating records for {student.name}. Leave blank to keep current value.")

        new_name = input(f"Enter new name ({student.name}): ").strip()
        if new_name:
            student.name = new_name

        new_age_str = input(f"Enter new age ({student.age}): ").strip()
        if new_age_str:
            try:
                student.age = int(new_age_str)
            except ValueError:
                print("Invalid age entered. Keeping old age.")

        new_grade = input(f"Enter new grade ({student.grade}): ").strip()
        if new_grade:
            student.grade = new_grade

        self.save_to_file()
        print("Student updated successfully!")

    def delete_student(self):
        """Delete a student record."""
        print("\n--- Delete Student ---")
        roll_no = input("Enter Roll Number to delete: ").strip()
        if roll_no in self.students:
            del self.students[roll_no]
            self.save_to_file()
            print("Student deleted successfully!")
        else:
            print("Student not found.")

def main():
    manager = StudentManager()
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_student()
        elif choice == '5':
            manager.delete_student()
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 6.")

if __name__ == "__main__":
    main()
