inp = open("Input/numbers.txt", "r")
out = open("Output/output04.txt", "w")

for line in inp:
    son = int(line.strip())
    if son % 2 == 0:
        out.write(str(son) + "\n")

print("juft sonlarni chiqarish bajarildi")

inp.close()
out.close()
