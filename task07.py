with open("Input/numbers.txt") as f:
    numbers = list(map(int, f))
kvadratlar = list(map(lambda x: x**2, numbers))

with open("Output/output07.txt", "w") as out:
    for num, kv in zip(numbers, kvadratlar):
        out.write(f"{num}^2 = {kv}\n")
