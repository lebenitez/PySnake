import curses

def game_loop(window):
    # Setup Inicial
    curses.curs_set(0)
    personagem = [10,15]
    current_direction = curses.KEY_RIGHT

    while True:
        draw_screen(window=window)
        draw_actor(actor=personagem, window=window)
        direction = get_new_direction(window=window, timeout=100) # O tempo de timeout determina a velocidade do actor, quanto menor o timeout, mais rápido
        if direction is None:
            direction = current_direction
        move_actor(actor=personagem, direction=direction)
        if actor_hit_border(actor=personagem, window=window):
            return
        current_direction = direction
    
def draw_screen(window):
    window.clear()
    window.border(0)

def draw_actor(actor, window):
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)

def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_RIGHT, curses.KEY_DOWN, curses.KEY_LEFT]:
        return direction
    return None

def move_actor(actor, direction):
        match direction:
            case curses.KEY_UP:
                actor[0] -= 1
            case curses.KEY_RIGHT:
                actor[1] += 1
            case curses.KEY_DOWN:
                actor[0] += 1
            case curses.KEY_LEFT:
                actor[1] -= 1

def actor_hit_border(actor, window):
    height, width = window.getmaxyx()
    if (actor[0] <= 0) or (actor[0] >= height-1):
        return True
    if (actor[1] <= 0) or (actor[1] >= width-1):
        return True
    return False
    
if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Perdeu!')

