with open("Input/numbers.txt") as f:
    numbers = list(map(int, f))
toq_sonlar = list(filter(lambda x: x % 2 == 1, numbers))

with open("Output/output06.txt", "w") as out:
    for son in toq_sonlar:
        out.write(str(son) + "\n")
