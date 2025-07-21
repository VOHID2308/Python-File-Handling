from collections import Counter

with open("INput/grades.csv", "r") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
grade_count = Counter(grades)

with open("Output/output23.txt", "w") as out:
    for grade, count in grade_count.items():
        out.write(f"Baho {grade}: {count} marta\n")
