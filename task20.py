with open("Input/grades.csv", "r") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
average = sum(grades) / len(grades)

with open("Output/output20.txt", "w") as out:
    out.write(f"O'rtacha baho: {round(average, 2)}")
