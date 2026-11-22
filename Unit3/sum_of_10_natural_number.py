# Program: Find addition of first ten natural numbers using while loop

count, add = 1, 0           # initialize
while count <= 10:          # condition
    add = add + count
    count += 1              # increment
print('Addition is=', add)