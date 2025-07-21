with open("Input/grades.csv", "r") as file:
    lines = file.readlines()[1:]

with open("Output/high_scores.csv", "w") as out:
    out.write("Name,Grade\n")
    for line in lines:
        name, grade = line.strip().split(",")
        if int(grade) == 5:
            out.write(f"{name},{grade}\n")
