#מיקום צוללות אקראי #
import random
def place_random_ships(ships: list[list[int]], n: int) -> None:
    #
    for i in range(n):
        numx = random.randint(0,len(ships)-1)
        numy = random.randint(0,len(ships)-1)
        while ships[numx][numy] == 1:
            numx = random.randint(0,len(ships)-1)
            numy = random.randint(0,len(ships)-1)
        ships[numx][numy] = 1
    return None


