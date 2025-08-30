# Student Record System
student_info=() #Tuple
course_enrollment=[] #List
print("Welcome to the Student Management System")
print("Enter your choice:\n1. Add Student\n2. Enroll in Course\n3. View Students\n4. view enrolled courses\n5. Exit")
while True:
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        id=int(input("Enter your ID:"))
        age = input("Enter student age: ")
        student_info = (name,id,age)
        print(f"Student {name} id {id} added successfully.")
        
    elif choice == '2':
        if not student_info:
            print("No student information available. Please add a student first.")
            continue
        course = input("Enter course name to enroll in: ")
        course_enrollment.append((student_info[0], course))
        print(f"{student_info[0]} enrolled in {course}.")
        
    elif choice == '3':
        if not student_info:
            print("No students available.")
        else:
            print(f"Student Name: {student_info[0]}, ID: {student_info[1]}, Age: {student_info[2]}")
            
    elif choice == '4':
        if not course_enrollment:
            print("No courses enrolled.")
        else:
            for student, course in course_enrollment:
                print(f"{student} is enrolled in {course}.")
                
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
