def average_grade(grades):
    result = sum(grades)/len(grades)
    return result


n = int(input())
students = {}

for _ in range(n):
    student_data = input().split()
    name, grade = student_data
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    average = average_grade(grades)
    grades_strings = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f"{student} -> {grades_strings} (avg: {average:.2f})")