# ---------- Take input from user ----------
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

# ---------- Method 1 : Using 'and' operator ----------
if (a >= b) and (a >= c):
    greatest = a
elif (b >= a) and (b >= c):
    greatest = b
else:
    greatest = c
print(f"Method 1 - The greatest number is: {greatest}")

# ---------- Method 2 : Short hand if...else ----------
greatest = a if (a >= b and a >= c) else (b if b >= c else c)
print(f"Method 2 - The greatest number is: {greatest}")

# ---------- Method 3 : Using max() function ----------
greatest = max(a, b, c)
print(f"Method 3 - The greatest number is: {greatest}")
