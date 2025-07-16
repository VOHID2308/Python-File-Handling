with open("Input/students.txt") as f:
    names = list(map(str.strip, f))

long_names = filter(lambda name: len(name) > 5, names)

with open("Output/output16.txt", "w") as out:
    for name in long_names:
        out.write(name + "\n")
