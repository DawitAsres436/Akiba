def validate_score(score):
    if score < 0 or score > 100:
        return False
    return True


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students):
    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)


def find_highest_score(students):
    highest = students[0]["score"]

    for student in students:
        if student["score"] > highest:
            highest = student["score"]

    return highest


def find_lowest_score(students):
    lowest = students[0]["score"]

    for student in students:
        if student["score"] < lowest:
            lowest = student["score"]

    return lowest


def count_passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


def students_above_average(students, average):
    above_average = []

    for student in students:
        if student["score"] > average:
            above_average.append(student)

    return above_average


def generate_report(students):
    average = calculate_average(students)
    highest = find_highest_score(students)
    lowest = find_lowest_score(students)

    passed, failed = count_passed_failed(students)

    above_average = students_above_average(students, average)

    print("\n========== STUDENT REPORT ==========")

    for student in students:
        grade = calculate_grade(student["score"])

        print(
            f'Name: {student["name"]} | '
            f'Score: {student["score"]} | '
            f'Grade: {grade}'
        )

    print("------------------------------------")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")

    print("\nStudents above class average:")

    for student in above_average:
        print(f'{student["name"]} - {student["score"]}')

    print("====================================")


# Student data

students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]


valid = True

for student in students:
    if not validate_score(student["score"]):
        print(f'Invalid score for {student["name"]}')
        valid = False

if valid:
    generate_report(students)