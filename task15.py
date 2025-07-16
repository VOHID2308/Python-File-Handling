with open("Input/students.txt") as f:
    names = list(map(str.strip, f))

with open("Output/output15.txt", "w") as out:
    for name in names:
        out.write(f"{name} — {len(name)} harf\n")
