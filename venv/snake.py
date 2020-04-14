import random
import curses

class Snake:
    #head = 0
    body = 0
    move_snake = 0
    grow = 0
class Food:
    position = 0
    new = 0
    remove = 0 
class Game:
    key = 0
    snk_x = 0
    snk_y = 0



def update_snake(snake, action = 'move'):

    if action == 'move':
        w.addch(Snake.body[0], Snake.body[1], ' ')
        w.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
        for part in snake[1:]:
            w.addch(part[0], part[1], curses.ACS_CKBOARD)

    elif action == 'eat':
        w.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
        for part in snake[1:]:
            w.addch(part[0], part[1], curses.ACS_CKBOARD)
    else:
        pass


def adding_info(food=0, length=3, width=0):
    Snake.grow = length
    separator = (width-1) * '*'
    w.addstr(1, 0, separator)
    w.addstr(0 , 3, "Length of snake: " + str(Snake.grow))
    w.addstr(0, int(width/2), "Food eaten: " + str(food))
###############################################################################

# initialize the screeen
s = curses.initscr()
curses.curs_set(0)


sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)
curses.COLOR_RED
Game.snk_x = int(sw/4)
Game.snk_y = int(sh/2)

snake = [
    [Game.snk_y, Game.snk_x],
    [Game.snk_y, Game.snk_x-1],
    [Game.snk_y, Game.snk_x-2]
    ]

food = [int(sh/2), int(sw/2)]
w.addch(food[0], food[1], curses.ACS_DIAMOND)

Game.key = curses.KEY_RIGHT

Food.new = 0
Snake.grow = len(snake)

while True:
    offset = 2
    adding_info(Food.new, Snake.grow, int(sw))
    next_key = w.getch()
    Game.key = Game.key if next_key == -1 else next_key

    if snake[0][0] in [offset-1, sh-1] or snake[0][1] in [0, sw-1] or snake[0] in snake[1:]:
        curses.endwin()
        print("Game Over")
        print("You results: snake length = %d , food eaten: = %d" % (Snake.grow, Food.new))
        quit()
    elif Game.key == 113: # pressing "q" will quite the game
        curses.endwin()
        print("User exit the game")
        quit()
    else:
        Snake.move = [snake[0][0], snake[0][1]]

        if Game.key == curses.KEY_DOWN:
            Snake.move[0] += 1
        if Game.key == curses.KEY_UP:
            Snake.move[0] -= 1
        if Game.key == curses.KEY_LEFT:
            Snake.move[1] -= 1
        if Game.key == curses.KEY_RIGHT:
            Snake.move[1] += 1

        snake.insert(0, Snake.move)

        if snake[0] == food:
            food = None
            Food.new += 1
            Snake.grow += 1
            while food is None:
                Food.position = [
                    random.randint(1, sh-offset),
                    random.randint(1, sw-1)
                ]
                food = Food.position if Food.position not in snake else None
            w.addch(food[0], food[1], curses.ACS_DIAMOND)
            update_snake(snake, 'eat')
            Food.remove=+1

        else:
            Snake.body = snake.pop()
            update_snake(snake, 'move')

