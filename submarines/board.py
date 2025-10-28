#יצירה/עדכון/תצוגת לוח #
def create_matrix(size:int = 5, fill: int = 0) -> list[list[int]]:
    
    mat = []
    for i in range(size):
        mat.append([])
        for j in range(size):
            mat[i].append(fill)
    return mat

def create_rifle():
    size = int(input("enter size rifle"))
    return size

def create_Submarines():
    size = int(input("enter size Submarines"))
    return size


def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    mat = []
    for i in range(size):
        mat.append([])
        for j in range(size):
            mat[i].append(fill)
    return mat


def in_bounds(size: int, x: int, y: int) -> bool:
    if x <= size and y <= size:
        return True
    return False

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    ship_count = 0
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i][j] == 1 and shots[i][j] == False:
                ship_count += 1
    return ship_count

def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    bourd = ""
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i][j] == 1 and shots[i][j] == True:
                bourd += 'v'
            elif ships[i][j] == 0 and shots[i][j] == True:
                bourd += 'x'
            else:
                bourd += 'o'
    return bourd

def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    bourd = ""
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i][j] == 1 and shots[i][j] == True:
                bourd += 'v1'
            elif ships[i][j] == 1 and shots[i][j] == False:
                bourd += 'x1'
            else:
                bourd += 'o'
    return bourd

def update_quantity(state:dict) -> dict:
    state["shots_used"] -= 1
    return state

def is_shots(x:int,y:int,state) -> bool:
    if state["shots"][x][y] == True:
        return True
    return False