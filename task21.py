with open("Input/grades.csv", "r") as file:
    lines = file.readlines()[1:]

max_grade = -1
top_students = []

for line in lines:
    name, grade = line.strip().split(",")
    grade = int(grade)
    if grade > max_grade:
        max_grade = grade
        top_students = [name]
    elif grade == max_grade:
        top_students.append(name)

with open("Output/output21.txt", "w") as out:
    out.write(f"Eng yuqori baho: {max_grade}\n")
    out.write("Top oquvchilar: " + ", ".join(top_students))
