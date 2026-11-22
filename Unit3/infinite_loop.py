# Program: Infinite loop
# The counter change (num += 1) is missing, so the condition num < 10
# never becomes False and the loop runs forever.
# Press Ctrl + C in the terminal to stop it.

num = 0                     # initialize
while num < 10:             # condition
    print(num, end=" ")
    # counter change is missing
print("end")