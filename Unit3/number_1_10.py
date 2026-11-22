# Program: Print numbers 1 to 10
# Variations: 1) else statement for while  2) single statement while

# ---------- Variation 1 : else statement for while loop ----------
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
else:
    print("end")

# ---------- Variation 2 : Single statement while ----------
# statements are written on one line, separated by semicolon
num = 1
while num <= 10: print(num, end=" "); num += 1
print()