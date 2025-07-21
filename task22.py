with open("Input/grades.csv", "r") as file:
    lines = file.readlines()[1:]

count_5 = sum(1 for line in lines if int(line.strip().split(",")[1]) == 5)

with open("Output/output22.txt", "w") as out:
    out.write(f"Bahosi 5 bo'lganlar soni: {count_5}")
