## כניסה נקודת) CLI)
import submarines.board
import submarines.game
import submarines.io
import submarines.placement

def play() -> None:
    # size: int = 6, n_ships: int = 6, max_shots: int = 10, *, one_based: bool = True
     state_ship = submarines.game.init_game(submarines.io.size_mat(),submarines.board.create_Submarines(),submarines.board.create_rifle())
     submarines.placement.place_random_ships(state_ship["ships"],state_ship["size"])

    #  while not submarines.game.is_lost(state_ship):
     while submarines.game.is_lost(state_ship) == False:
        bourd = submarines.board.render_public(state_ship["ships"],state_ship["shots"])
        print (bourd)
        submarines.game.shoot(state_ship)
        if submarines.game.is_won(state_ship):
            submarines.io.print_end(state_ship,True)
            return
        elif submarines.game.is_lost(state_ship):
               submarines.io.print_end(state_ship,False)
               return
        # state_ship["shots_used"] = submarines.board.update_quantity(state_ship)
        state_ship["shots_used"] -= 1
        

if __name__ == "__main__":
     play()
          
               
               


