with open("Input/grades.csv", "r") as file:
    lines = file.readlines()

with open("Output/output19.txt", "w") as out:
    for line in lines:
        name, grade = line.strip().split(",")
        out.write(f"{name}: {grade}\n")
