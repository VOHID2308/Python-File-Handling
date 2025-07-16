with open("Input/students.txt") as f:
    names = list(map(str.strip, f))

with open("Output/output12.txt", "w") as out:
    out.write("Ismlar soni: " + str(len(names)))
