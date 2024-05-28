n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=" ")
    print()
   # Iteration:--    
#  The outer loop (for i in range(1, n + 1)) iterates over each row, with i representing the iteration number.
# The inner loop (for j in range(1, n + 1)) iterates n times to print the iteration number i in each position.
# print(i, end=" ") prints the iteration number i followed by a space without moving to the next line.
# After printing the iteration numbers for each position in the inner loop, print() is used to move to the next line, starting a new row.
# Output:
# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4 
