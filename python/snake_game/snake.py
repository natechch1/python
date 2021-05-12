import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# setup window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)   # y,x
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1) # -1

# user name
# user_name = window.get_wch()

# set initial snake and food
snake = [[4,10], [4,9], [4,8]]
food = [10,20]

window.addch(food[0], food[1], "@")

# game part
ECS = 27
key = KEY_RIGHT
score = 0

while key != ECS:
    window.addstr(0, 2, 'Score ' + str(score) + ' ')   #add the score
    window.timeout(150 - (len(snake)//5 + len(snake)//10)%120) # increase speed

    # prev_key = key
    # event = window.getch()
    # key = event if event != -1 else prev_key  # what this prev_key here mean?
    prev_key = key                                                  # Previous key pressed
    event = window.getch()
    key = key if event == -1 else event 

    if key == ord(' '):                               # If SPACE BAR is pressed, wait for another
        key = -1                                      # one (Pause/Resume)
        while key != ord(' '):
            key = window.getch()
        key = prev_key
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, ECS]:
        key = prev_key

    # for the next coordinates
    y = snake[0][0]
    x = snake[0][1] 

    if key == KEY_DOWN:
        y += 1
    if key == KEY_UP:
        y -= 1
    if key == KEY_LEFT:
        x -= 1
    if key == KEY_RIGHT:
        x += 1

    snake.insert(0, [y, x]) # use append will be faster

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1


    # break if the snake runs over itself
    if snake[0] in snake[1:]: break

    # if the snake eat the food
    if snake[0] == food:
        score += 1
        food = []
        while food == []:  # find the next food
            food = [randint(1, 18), randint(1, 58)]
            if food in snake:
                food = []
        window.addch(food[0], food[1], "@") # show the new food coordinates in the screen 
    else:
        # move the snake
        last = snake.pop()
        window.addch(last[0], last[1], ' ')

    window.addch(snake[0][0], snake[0][1], "*")

# end window
curses.endwin()
print(f"Final score = {score}")