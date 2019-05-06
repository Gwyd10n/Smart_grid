def create_test_grid():
    grid = []
    for y in range(10):
        row = []
        for x in range(10):
            if y == 2 and x == 3:
                row.append('H')
            elif y == 8 and x == 9:
                row.append('B')
            else:
                row.append(0)
        grid.append(row)
    return grid

if __name__ == "__main__":
    grid = create_test_grid()

    for row in grid:
        print(row)
