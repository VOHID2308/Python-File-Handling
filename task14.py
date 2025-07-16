with open("Input/students.txt") as f:
    names = sorted(map(str.strip, f), reverse=True)

with open("Output/output14.txt", "w") as out:
    for name in names:
        out.write(name + "\n")
