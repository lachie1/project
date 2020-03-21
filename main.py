
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 85
HEIGHT = 85
 
# This sets the margin between each cell
MARGIN = 1
 
#PLAYER INSTRUCTIONS


# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
number = 1
for row in range(3):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(3):
        grid[row].append(number)  # Append a cell
        number = number + 1


grid[2][2] = ""
print(grid[1][0])
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Number Puzzle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32) 
  
# create a text suface object, 
# on which text is drawn on it. 
# ---------- MAINFRAME FUNCTION -------------
def acceptmove(typed):
  print(typed)
  position = "invalid"
  for row in range(3):
    for column in range(3):
      if grid[row][column] == "":
        position = [row,column]
  print(position)
  if typed == "Up":
    if position[0] != 0:
      print(position[0])
      print("Invalid Move")
      return
    else:
      middle = grid[1][position[1]]
      top = grid[2][position[1]]
      grid[0][position[1]] = middle
      grid[1][position[1]] = top
      grid[2][position[1]] = ""
  elif typed == "Down":
    if position[0] != 2:
      print(position[0])
      print("Invalid Move")
      return
    else:
      middle = grid[1][position[1]]
      bottom = grid[0][position[1]]
      grid[2][position[1]] = middle
      grid[1][position[1]] = bottom
      grid[0][position[1]] = ""
  elif typed == "Left":
    if position[1] != 0:
      print(position[1])
      print("Invalid Move")
      return
    else:
      middle = grid[position[0]][1]
      right = grid[position[0]][2]
      grid[position[0]][0] = middle
      grid[position[0]][1] = right
      grid[position[0]][2] = ""
  elif typed == "Right":
    if position[1] != 2:
      print(position[1])
      print("Invalid Move")
      return
    else:
      middle = grid[position[0]][1]
      left = grid[position[0]][0]
      grid[position[0]][1] = left
      grid[position[0]][2] = middle
      grid[position[0]][0] = ""

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
 #           grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column, "Selected Tile: ",grid[row][column])
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            print("Player moved up!")
            acceptmove("Up")
          elif event.key == pygame.K_a:
            print("Player moved left!")
            acceptmove("Left")
          elif event.key == pygame.K_s:
            print("Player moved down!")
            acceptmove("Down")
          elif event.key == pygame.K_d:
            print("Player moved right!")
            acceptmove("Right")

 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(3):
        for column in range(3):
            color = WHITE
            if grid[row][column] == "":
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            text = font.render(str(grid[row][column]), 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.center = ((((MARGIN + WIDTH) * column + MARGIN) + 40),((MARGIN + HEIGHT) * row + MARGIN)+40)
            screen.blit(text, textpos)
 #           pygame.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
