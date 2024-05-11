submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_and_attended = []

"""Task 1: Given the two lists:
Find out which students both submitted their assignments and attended the class.
"""
for i in range(len(submitted)):
    for x in range(len(attended)):
        if (submitted[i] == attended[x]):
            submitted_and_attended.append(submitted[i])

print('These Two Students Submitted and Attended: ', submitted_and_attended)

"""Task 2: Check if the two lists are identical in terms of their content, regardless of order."""
submitted.sort()
attended.sort()
print('Are The Lists Identical?: ', submitted == attended)

"""Task 3: Using list methods, remove any student from the attended list who did not submit their assignment."""
attended = [student for student in attended if student in submitted_and_attended]

print('New List Removing Students Who Did Not Submit: ', attended)