#לוגיקת משחק וחוקי עצירה #
import submarines.board
import submarines.io
import random
def init_game(size: int, n_ships: int, max_shots: int) -> dict:
   #, *, rng: random.Random | None = None
   state_ship = {
                "size": size,
                "ships": submarines.board.create_matrix(size),
                "shots": submarines.board.create_bool_matrix(size),
                "n_ships": n_ships,
                "max_shots": max_shots,
                "shots_used": max_shots
                }
   return state_ship

def shoot(state: dict) -> tuple[bool, str]:
    num_x = int(input("enter for x"))
    num_y = int(input("enter for y"))
    if submarines.board.is_shots(num_x,num_y,state):
        print("errore is true")
        shoot(state)
    if not submarines.board.in_bounds(state["size"],num_x,num_y):
        print("eerrore is out of range")
        shoot(state)
    state["shots"][num_x][num_y] = True
    submarines.board.update_quantity(state)
    
    return state

def is_won(state: dict) -> bool:
    for i in range(state["size"]):
        for j in range(state["size"]):
            if state["ships"][i][j] == 1 and state["shots"][i][j] == False:
                return False
    return True

def is_lost(state: dict) -> bool:
    if state["shots_used"] == 0:
        return True
    return False

def num_ship(state) -> int:
    count = 0
    for i in range(len(state["size"])):
        for j in range(len(state["size"])):
            if state["ships"][i][j] == 1 and state["shots"][i][j] == False:
                count += 1
    return count


   