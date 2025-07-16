with open("Input/students.txt") as f:
    names = list(map(str.strip, f))

a_names = filter(lambda name: name.startswith("A"), names)

with open("Output/output17.txt", "w") as out:
    for name in a_names:
        out.write(name + "\n")
