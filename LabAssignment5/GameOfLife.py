import numpy
# this is the function with all the rules
def play_life(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid & Stasis (if a living cell is surrounded by two or three living cells, it survives)
    for x in range(xmax):
        for y in range(ymax):
            n = numpy.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # Overpopulation (if a living cell is surrounded by more than three living cells, it dies) and Underpopulation (if a living cell is surrounded by fewer than two living cells, it dies)
            elif n == 3:
                b[x, y] = 1 # Reproduction (if a dead cell is surrounded by exactly three cells, it becomes a live cell)
    return(b)

# (5,5) is just a sample which can be replaced
life = numpy.zeros((5, 5), dtype=numpy.byte)

# starting conditions
life[2, 1:4] = 1 # a spinner

# starting the game
print(life)
for i in range(3):
    life = play_life(life)
    print(life)