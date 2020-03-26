
import pygame
import random

def BootUp():
  print("Config Booting Globals")
  ####################################
  global BLACK
  global WHITE
  global GREEN
  global RED
  global WIDTH
  global HEIGHT
  global MARGIN
  global grid
  global number
  global counter
  global WINDOW_SIZE
  global done
  global screen
  global clock
  global font
  global font2
  global countertext
  global textpos2
  ####################################
  print("Global Booting Values")
  ####################################
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  GREEN = (0, 255, 0)
  RED = (255, 0, 0)
  WIDTH = 85
  HEIGHT = 85
  MARGIN = 1
  grid = []
  number = [1,2,3,4,5,6,7,8,""]
  number2 = 0
  counter = "0"
  WINDOW_SIZE = [500, 255]
  done = False
  ##################################
  print("Booting Grid Setup")
  ##################################
  random.shuffle(number)
  for row in range(3):
    grid.append([])
    for column in range(3):
        grid[row].append(number[number2])  # Append a cell
        number2 = number2 + 1
  #################################
  print("Booting Pygame Init")
  #################################
  pygame.init()
  screen = pygame.display.set_mode(WINDOW_SIZE)
  pygame.display.set_caption("Number Puzzle")

  clock = pygame.time.Clock()
  font = pygame.font.Font('freesansbold.ttf', 32) 
  font2 = pygame.font.Font('freesansbold.ttf', 22) 
  countertext = font2.render(("Move Counter:" + counter), 1, (255, 255, 255))
  textpos2 = countertext.get_rect()
  textpos2.center = (350,20)


BootUp()

# ---------- MAINFRAME FUNCTION -------------
def acceptmove(typed, inputpos):
  global counter
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
      counter = str(int(counter) + 1)
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
      counter = str(int(counter) + 1)
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
      counter = str(int(counter) + 1)
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
      counter = str(int(counter) + 1)
  elif typed == "Mouse":
    #mousefunc
    if position[0] == inputpos[0] and (position[1]+1 == inputpos[1] or position[1]-1 == inputpos[1]):
      print("yes")
      print(position, inputpos)
      grid[position[0]][position[1]] = grid[inputpos[0]][inputpos[1]]
      grid[inputpos[0]][inputpos[1]] = ""
      counter = str(int(counter) + 1)
    elif position[1] == inputpos[1] and (position[0]+1 == inputpos[0] or position[0]-1 == inputpos[0]):
 #     grid[position[0][position[1]] = grid[inputpos[0]][inputpos[1]]
      grid[position[0]][position[1]] = grid[inputpos[0]][inputpos[1]]
      grid[inputpos[0]][inputpos[1]] = ""
      print("h")
      counter = str(int(counter) + 1)
      print(counter)
    else:
      print("No")
  checkwin()

def checkwin():
  global done
  checker = []
  for number in range(3):
    for entry in grid[number]:
      checker.append(entry)
  if checker[8] == "":
    checker[8] = 0
    valuex = False
    for number in range(8):
      if int(checker[number-1]) == int(checker[number]) - 1:
        valuex = True
      else:
        print(int(checker[number-1]), int(checker[number]))
        valuex = False
    if valuex == True:
      done = True
      print("##########################")
      print("WIN")
      print("##########################")
    checker[8] = ""


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            info = [row,column]
            print("Click ", pos, "Grid coordinates: ", row, column, "Selected Tile: ",grid[row][column])
            acceptmove("Mouse", info)
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            print("Player moved up!")
            acceptmove("Up", "none")
          elif event.key == pygame.K_a:
            print("Player moved left!")
            acceptmove("Left", "none")
          elif event.key == pygame.K_s:
            print("Player moved down!")
            acceptmove("Down", "none")
          elif event.key == pygame.K_d:
            print("Player moved right!")
            acceptmove("Right", "none")
          elif event.key == pygame.K_r:
            print("Restarting Game!")
            BootUp()

    screen.fill(BLACK)
 

    for row in range(3):
        for column in range(3):
            color = WHITE
            if grid[row][column] == "":
                color = GREEN
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
            text = font.render(str(grid[row][column]), 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.center = ((((MARGIN + WIDTH) * column + MARGIN) + 40),((MARGIN + HEIGHT) * row + MARGIN)+40)
            screen.blit(text, textpos)
    countertext = font2.render(("Move Counter:" + counter), 1, (255, 255, 255))
    screen.blit(countertext, textpos2)

    clock.tick(120)

    pygame.display.flip()


pygame.quit()
