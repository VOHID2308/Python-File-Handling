with open("Input/grades.csv", "r") as file:
    lines = file.readlines()[1:]

students = []
grades = []

for line in lines:
    name, grade = line.strip().split(",")
    grade = int(grade)
    students.append((name, grade))
    grades.append(grade)

avg = sum(grades) / len(grades)

with open("Output/output24.txt", "w") as out:
    for name, grade in students:
        if grade > avg:
            out.write(name + "\n")
