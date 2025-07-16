with open("Input/students.txt") as f:
    names = sorted(map(str.strip, f))

with open("Output/output13.txt", "w") as out:
    for name in names:
        out.write(name + "\n")
