import copy, random, sys, time

WIDTH = 50
HEIGHT = 20
ALIVE = '|'
DEAD = '-'
nextCells = {}


def main():
    # write a reading file function to copy a simulation to nextCells
    # for x first or for y first?
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.randint(0, 4) == 0:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD
    while True:
        print('\n' * 50)
        # cells = nextCells ?
        cells = copy.deepcopy(nextCells)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(cells[(x, y)], end='')
            print()
        print("Press ctrl + C to quit the program.")

        for x in range(WIDTH):
            for y in range(HEIGHT):
                left = (x - 1) % WIDTH
                right = (x + 1) % WIDTH
                above = (y - 1) % HEIGHT
                below = (y + 1) % HEIGHT

                numberNeighbors = 0
                if cells[(left, above)] == ALIVE:
                    numberNeighbors += 1
                if cells[(x, above)] == ALIVE:
                    numberNeighbors += 1
                if cells[(right, above)] == ALIVE:
                    numberNeighbors += 1
                if cells[(left, y)] == ALIVE:
                    numberNeighbors += 1
                if cells[(right, y)] == ALIVE:
                    numberNeighbors += 1
                if cells[(left, below)] == ALIVE:
                    numberNeighbors += 1
                if cells[(x, below)] == ALIVE:
                    numberNeighbors += 1
                if cells[(right, below)] == ALIVE:
                    numberNeighbors += 1

                if cells[(x, y)] == ALIVE and (numberNeighbors == 2 or numberNeighbors == 3):
                    nextCells[(x, y)] = ALIVE
                elif cells[(x, y)] == DEAD and numberNeighbors == 3:
                    nextCells[(x, y)] = ALIVE
                else:
                    nextCells[(x, y)] = DEAD
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Goodbye")
            sys.exit()


if __name__ == "__main__":
    main()

"""
1. It reduces the size of the game
2. The previous and the next simulations would be next to each other, making it hard to read.
3. It would be harder to keep the cells alive, making the game only have a few cells live.
There would also be fewer patterns of the cells.
4. After the initial simulation, all the cells are alive and stay consistent.
"""