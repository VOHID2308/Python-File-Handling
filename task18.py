ism = input("Ism kiriting: ").strip()

with open("Input/students.txt") as f:
    names = list(map(str.strip, f))

with open("Output/output18.txt", "w") as out:
    if ism in names:
        out.write("Bu ism faylda mavjud.")
    else:
        out.write("Bu ism faylda topilmadi.")
