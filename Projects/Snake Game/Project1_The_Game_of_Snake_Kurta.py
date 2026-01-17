"""
    Snake Game - Avoid running into the walls or the snake itself while you try to eat as 
    many food pieces as you can. The snake grows for every piece eaten.
    The background color randomizes every multiple of a configurable color interval (default is 5).

    Filename:       Project1_The_Game_of_Snake_Kurta.py
    Author:         Michael Kurta
    Date:           9/18/2025
    Course:         COMP 1353
    Assignment:     Project 1
    Collaborators:  None
    Internet Source:None
"""

import random
import dudraw
import sys

from doublyLinkedList2 import DoublyLinkedList

SNAKE_START_X = 10
SNAKE_START_Y = 7

# Width and length of each movement square
WIDTH       = 30

PIX_WIDTH   = 600

# Color interval
COLOR_INT   = 5

# Modifier for snake segment size
SCALE_CONST = 1.2

# Game action macros
COLLISION = -1
NO_ACTION = 0
SNAKE_FED = 1

UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

class Snake(DoublyLinkedList):

  def __init__(self, direction: int = UP, x_block: int = SNAKE_START_X, y_block: int = SNAKE_START_Y, length = 6):
    super().__init__()
    self.dir    = direction
    self.x      = x_block
    self.y      = y_block
    self.last_x = None      # x and y Used to track where to place a new segment
    self.last_y = None
    self.length = length

    if self.length > SNAKE_START_Y:
      raise ValueError(f"Starting length cannot be greater than {SNAKE_START_Y}.")
    # Virtually count down using size
    while length > 0:
      self.add_last(self.x, self.y)
      self.y      -= 1
      length      -= 1

  def add_last(self, x, y):
    """
  Adds a segment to the snake body
  parameters: 
            x :
              x coordinate of snake from 1-20
            y :
              y coordinate of snake from 1-20
  returns
      None
  """
    super().add_last(x, y)
    self.x = x
    self.y = y

  def draw_head(self):
    """
  Draws the head of the snake
  parameters: None
  returns
      None
  """
    x = (self.header.next.x - 0.5) * WIDTH
    y = (self.header.next.y - 0.5) * WIDTH
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_square(x, y, PIX_WIDTH / (SCALE_CONST*WIDTH))
    match self.dir:
      
      case 0:   # Up
        dudraw.set_pen_color(dudraw.WHITE)
        dudraw.filled_circle(x + 4, y + 4, 2 )
        dudraw.filled_circle(x - 4, y + 4, 2 )
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(x, y + 22, 3, 7)

      case 1:   # Right
        dudraw.set_pen_color(dudraw.WHITE)
        dudraw.filled_circle(x + 4, y + 4, 2 )
        dudraw.filled_circle(x + 4, y - 4, 2 )
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(x + 22, y, 7, 3)

      case 2:   # Down
        dudraw.set_pen_color(dudraw.WHITE)
        dudraw.filled_circle(x + 4, y - 4 , 2 )
        dudraw.filled_circle(x - 4, y - 4, 2 )
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(x, y - 22, 3, 7)

      case 3:   # Left
        dudraw.set_pen_color(dudraw.WHITE)
        dudraw.filled_circle(x - 4, y + 4, 2 )
        dudraw.filled_circle(x - 4, y - 4, 2 )
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(x - 22, y, 7, 3)


    dudraw.set_pen_color(dudraw.BLACK) 
    #dudraw.filled_rectangle(285, 195, 15, 15)

  def grow(self):
    """
  Grows the length of the snake
  parameters: None
  returns
      None
  """
    self.add_last(self.last_x, self.last_y)
    self.size += 1

class Game:

  def __init__(self):

    self.running  = True
    self.num_eats = 0
    self.food_x   = 10
    self.food_y   = 16
    self.r        = 0
    self.g        = 200
    self.b        = 0

    dudraw.set_canvas_size(PIX_WIDTH, PIX_WIDTH)
    dudraw.set_x_scale(0, PIX_WIDTH)
    dudraw.set_y_scale(0, PIX_WIDTH)
    dudraw.clear(dudraw.GREEN)
    dudraw.set_font_size(24)

    dudraw.set_pen_color(dudraw.WHITE)
    dudraw.text(300, 290, "Press Spacebar to begin")
    ## While loop polling for space press

    space_not_pressed = True
    while space_not_pressed:
      if dudraw.has_next_key_typed():
        k = dudraw.next_key_typed()

        if   k == ' ':
          space_not_pressed = False
      dudraw.show(10)


  def draw_game(self, snake: Snake):
    """
  Draws all of the objects in the game
  parameters: 
            snake : Snake object
            
  returns
      None
  """
    
    # Randomize the background color if self.num_eats is equal to a multiple of COLOR_INT
    if self.num_eats % COLOR_INT == 0 and self.num_eats > 0:
      self.r = random.randint(100, 255)
      self.g = random.randint(100, 255)
      self.b = random.randint(100, 255)

    # Reset the background
    dudraw.clear_rgb(self.r, self.g, self.b)
  
    # Draw the snake's head
    snake.draw_head()

    # Draw the food
    dudraw.set_pen_color(dudraw.ORANGE)
    dudraw.filled_square((self.food_x - 0.5)* WIDTH, (self.food_y - 0.5)* WIDTH, PIX_WIDTH / (SCALE_CONST*WIDTH))

    # Draw all of the snake body segments
    current = snake.header.next.next
    while current is not snake.tailer:
      dudraw.set_pen_color(dudraw.BLACK)
      x = float(current.x) - 0.5    # e.g. first tile "1" becomes float 0.5
      y = float(current.y) - 0.5    # e.g. last tile "20" becomes float 19.5
      dudraw.filled_square(x * WIDTH, y * WIDTH, PIX_WIDTH / (SCALE_CONST*WIDTH))
      current  = current.next

  def quit(self):
    sys.exit()

  def read_controls(self, snake: Snake):
    if dudraw.has_next_key_typed():
      k = dudraw.next_key_typed()

      if   k == 'w' and snake.dir is not DOWN:
        snake.dir = UP

      elif k == 'a' and snake.dir is not RIGHT:
        snake.dir = LEFT

      elif k == 's' and snake.dir is not UP:
        snake.dir = DOWN

      elif k == 'd' and snake.dir is not LEFT:
        snake.dir = RIGHT

      elif k == '\x1b':
        self.quit()

  def respawn_food(self, snake: Snake):
    pos_free = False
  
    self.food_x = random.randint(1, 20)
    self.food_y = random.randint(1, 20)
    current = snake.header.next
    while not pos_free:
      pos_free = True
      while current is not snake.tailer:
        if current.x == self.food_x and current.y == self.food_y:
          pos_free = False
          self.food_x = random.randint(1, 20)
          self.food_y = random.randint(1, 20)
          current = snake.header

        current = current.next

      dudraw.set_pen_color(dudraw.ORANGE)
      dudraw.filled_square((self.food_x - 0.5) * WIDTH, (self.food_y - 0.5) * WIDTH, PIX_WIDTH / (SCALE_CONST*WIDTH))

  def update(self, snake: Snake)->int:
    # Check if the snake has run into an edge
    if (snake.dir == UP and snake.header.next.y >= 20) or (snake.dir == DOWN and snake.header.next.y <= 1) or (snake.dir == LEFT and snake.header.next.x <= 1) or (snake.dir == RIGHT and snake.header.next.x >= 20):
      print((snake.header.next.x, snake.header.next.y))
      return -1
    
    current = snake.tailer.prev

    # save the last location of the tail segment to add another one if snake has eaten
    snake.last_x = current.x
    snake.last_y = current.y

    # Advance the snake coordinates from tail to head (head coordinate is the same as the segment after it)
    while current is not snake.header.next:
      current.x = current.prev.x
      current.y = current.prev.y
      current = current.prev

    # Advance the head in the direction given
    current = snake.header.next
    match snake.dir:

      case 0:
        current.y += 1

      case 2:
        current.y -= 1

      case 3:
        current.x -= 1

      case 1:
        current.x += 1

    # check if the snake ate food and return 1 if so
    if snake.header.next.x == self.food_x and snake.header.next.y == self.food_y:
      self.num_eats += 1
      self.respawn_food(snake)
      return 1
    
    # Move current off of the snake head for the next operation
    current = snake.header.next.next

    # Check if the snake has run into itself. Loop through the values and see if any match the head's coordinates
    # Return -1 
    # Also update the coordinates of the segments
    while current is not snake.tailer:

      if snake.header.next.x == current.x and snake.header.next.y == current.y:
        return -1

      current = current.next

    return 0
  

def main():

  # Intitialize Snake and Game objects
  snake = Snake()
  game = Game()

  # Main game loop
  while game.running:

    # Draw the game for a period
    game.draw_game(snake)

    dudraw.show(200)

    # Read the keyboard
    game.read_controls(snake)
    action = game.update(snake)

    # End the game and print text if there's a collision
    if action == COLLISION:
      game.running = False
      dudraw.set_pen_color(dudraw.WHITE)
      if game.num_eats == 1:
        dudraw.text(300, 290, f"Game over. You fed the snake {game.num_eats} time.")
      
      else:
        dudraw.text(300, 290, f"Game over. You fed the snake {game.num_eats} times.")

    # Grow the snake if fed
    elif action == SNAKE_FED:
      snake.grow()

  # Keep screen on for several seconds to read the text (Game over, outside main loop)
  dudraw.show(5000)

if __name__ == "__main__":
 main()