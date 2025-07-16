inp = open("Input/numbers.txt", "r")
out = open("Output/output08.txt", "w")

sana = 0
for line in inp:
    son = int(line.strip())
    if son % 5 == 0:
        out.write(str(son) + "\n")
        sana += 1

out.write("5 ga karrali sonlar soni: " + str(sana))
print("5 ga karrali sonlar soni amali bajarildi")

inp.close()
out.close()
