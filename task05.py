inp = open("Input/numbers.txt", "r")
out = open("Output/output05.txt", "w")

yigindi = 0
sana = 0

for line in inp:
    son = int(line.strip())
    yigindi += son
    sana += 1

orta = yigindi / sana
out.write("O'rtacha: " + str(orta))
print("O'rtacha son ani qlandi")

inp.close()
out.close()
