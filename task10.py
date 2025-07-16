with open("Input/numbers.txt") as f:
    numbers = sorted(map(int, f))

with open("Output/output10.txt", "w") as out:
    for son in numbers:
        out.write(str(son) + "\n")
