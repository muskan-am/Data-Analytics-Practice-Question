def print_zigzag(height, length):
    matrix = [[' ' for _ in range(length)] for _ in range(height)]
    row = 0
    down = True

    for col in range(length):
        matrix[row][col] = '*'
        
        if row == height - 1:
            down = False
        elif row == 0:
            down = True
        
        if down:
            row += 1
        else:
            row -= 1

    for line in matrix:
        print("".join(line))

print_zigzag(6, 21)