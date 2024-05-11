students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


"""Task 1: Given the lists:
Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"
"""
i = 0
while i < len(grades):
    if grades[i] < 80:
        print(f'Student Name: {students[i]}, Student Grade: {grades[i]}, Student Activity: {activities[i]} Will Be Removed')
        students.remove(students[i])
        activities.remove(activities[i])
        grades.remove(grades[i])
    i += 1

print(students, grades, activities)

"""Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]"""
students_approved = []

for i in range(len(students)):
    students_approved.append(students[i])


"""Task 3: Print the list students_approved"""
print('These Students Are Approved: ', students_approved)