# פלט/קלט) CLI)
import submarines.board
import submarines.game

def size_mat() -> int:
    size = int(input("enter size matritz"))
    # is_digit = size.isdigit()
    # if not is_digit:
    #     size_mat()
    return size


def print_status(state: dict) -> None:
    bourd = submarines.board.render_public(state)
    shoots = state["shots_used"]
    ship = submarines.game.num_ship(state)
    print(bourd)
    print("num shoot",shoots)
    print("num ship",ship)
    return None

def print_end(state: dict, won: bool) -> None:
    prt = submarines.board.render_reveal(state["ships"],state["shots"])
    if won:
        print("win")
    else:
        print("no win")
        print(prt)
    return None




