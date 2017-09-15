import libtcodpy as libtcod

def handle_keys(key):
    key_char = chr(key.c)

    xMove = 0
    yMove = 0

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        yMove -= 1
    if key.vk == libtcod.KEY_DOWN or key_char == 'j':
        yMove += 1
    if key.vk == libtcod.KEY_LEFT or key_char == 'h':
        xMove -= 1
    if key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        xMove += 1

    if(xMove != 0 or yMove != 0):
        return {'move': (xMove, yMove)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}
