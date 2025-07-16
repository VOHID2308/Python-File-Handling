inp = open("Input/numbers.txt", "r")
out = open("Output/output03.txt", "w")

max_son = -999999999
for line in inp:
    son = int(line.strip())
    if son > max_son:
        max_son = son

out.write("Eng katta son: " + str(max_son))
print("Eng katta son amali bajarildi ")

inp.close()
out.close()
