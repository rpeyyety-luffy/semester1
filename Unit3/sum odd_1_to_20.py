# Program: Addition of all odd numbers from 1 to 20 (1, 3, 5 ... 19)

count, add = 1, 0           # initialize
while count <= 20:          # condition
    add = add + count
    count += 2              # increment by 2
print('Addition is=', add)