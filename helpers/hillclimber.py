# evaluate the initial state. If it is a good state then return and exit.
# keep looping until we get a solution or there are no new operaters left.
# when found select and apply new operators
# evaluate the new state if
# a) it is a goal state then quit
# b) it is better than the current state make it the new current state.
# if it is not better, go back to step 2



def hillclimber(batteries, houses ):
    """
    Hillclimber algorithm.
    """


# get cables, capacity


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
