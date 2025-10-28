 ## Student Marks Calculator

# Function to calculate grade based on average marks
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

# Main program
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\n--- Enter details for Student {i+1} ---")
    name = input("Enter student name: ")
    
    marks = []
    subjects = int(input("Enter number of subjects: "))
    for j in range(subjects):
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)
    
    total = sum(marks)
    avg = total / subjects
    grade = calculate_grade(avg)
    
    student_info = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": avg,
        "Grade": grade
    }
    
    students.append(student_info)

# Display results
print("\n===== STUDENT REPORT =====")
for s in students:
    print(f"\nName: {s['Name']}")
    print(f"Marks: {s['Marks']}")
    print(f"Total: {s['Total']}")
    print(f"Average: {s['Average']:.2f}")
    print(f"Grade: {s['Grade']}")
