rows = 5
cols = 11

for i in range(rows):
    for j in range(cols):
        if j == 0 and i < rows - 1:
            print("*", end=" ")
        elif j == cols - 1 and i < rows - 1:
            print("*", end=" ")
        elif i == rows - 1:
            print("*", end=" ")
        elif i == j and j <= cols // 2:
            print("*", end=" ")
        elif i + j == cols - 1 and j >= cols // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
