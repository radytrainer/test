ROW = 3
COL = 4
array2D = []
# add star array
for row in range(ROW):
    array2D.append([])
    for col in range(COL):
        array2D[row].append('*')


# Print star
count = 0
while count < 3:
    count += 1
    x = int(input("X: "))
    y = int(input("Y: "))
    symbol = str(input("Symbol: "))
    array2D[x][y] = symbol
    result = ""
    for array in array2D:
        for star in array:
            result += star + " "
        result += '\n'
    print(result)