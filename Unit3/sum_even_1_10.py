# Program: Addition of even numbers from 1 to 10
# Variations: 1) range + for loop  2) range + for loop + if  3) only while loop

# ---------- Variation 1 : Range function and for loop ----------
total_sum = 0
for num in range(2, 11, 2):
    total_sum += num
print(f"The sum of even numbers between 1 and 10 is: {total_sum}")

# ---------- Variation 2 : Range function with for loop and if ----------
total_sum = 0
for num in range(1, 11):
    if num % 2 == 0:
        total_sum += num
print(f"The sum of even numbers between 1 and 10 is: {total_sum}")

# ---------- Variation 3 : Only while loop ----------
num = 2
total_sum = 0
while num <= 10:
    total_sum += num
    num += 2
print(f"The sum of even numbers between 1 and 10 is: {total_sum}")