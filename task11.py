with open("Input/students.txt") as f:
    names = list(map(str.strip, f))

with open("Output/output11.txt", "w") as out:
    for name in names:
        out.write(name + "\n")
        print(name)
