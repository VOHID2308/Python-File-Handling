with open("Input/numbers.txt") as f:
    numbers = list(map(int, f))

with open("Output/output09.txt", "w") as out:
    for son in numbers:
        xonalar = len(str(abs(son)))
        out.write(f"{son} — {xonalar} xonali\n")
