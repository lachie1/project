
import pygame
import random

config = {}

grid = []
number = [1,2,3,4,5,6,7,8,""]
number2 = 0

done = False

random.shuffle(number)
for row in range(3):
  grid.append([])
  for column in range(3):
    grid[row].append(number[number2])  # Append a cell
    number2 = number2 + 1
def BootUp():
  print("Config Booting Globals")
  ####################################
  config["BLACK"] = (0, 0, 0)
  config["WHITE"] = (255, 255, 255)
  config["GREEN"] = (0, 255, 0)
  config["RED"] = (255, 0, 0)
  config["WIDTH"] = 85
  config["HEIGHT"] = 85
  config["MARGIN"] = 1
  config["WINDOW_SIZE"]= [500, 255]
  config["COUNTER"] = "0"
  ##################################
  #################################
  print("Booting Pygame Init")
  #################################
  pygame.init()
#  screen = pygame.display.set_mode(config["WINDOW_SIZE"])
  pygame.display.set_caption("Number Puzzle")
  ################################
  print("Boot Complete")
  ################################

BootUp()

screen = pygame.display.set_mode(config["WINDOW_SIZE"])
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32) 
font2 = pygame.font.Font('freesansbold.ttf', 22) 


countertext = font2.render(("Move Counter:" + config["COUNTER"]), 1, (255, 255, 255))
textpos2 = countertext.get_rect()
textpos2.center = (350,20)

# ---------- MAINFRAME FUNCTION -------------
def acceptmove(typed, inputpos):
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
      config["COUNTER"] = str(int(config["COUNTER"]) + 1)
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
      config["COUNTER"] = str(int(config["COUNTER"]) + 1)
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
      config["COUNTER"] = str(int(config["COUNTER"]) + 1)
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
      config["COUNTER"] = str(int(config["COUNTER"]) + 1)
  elif typed == "Mouse":
    #mousefunc
    if position[0] == inputpos[0] and (position[1]+1 == inputpos[1] or position[1]-1 == inputpos[1]):
      print("yes")
      print(position, inputpos)
      grid[position[0]][position[1]] = grid[inputpos[0]][inputpos[1]]
      grid[inputpos[0]][inputpos[1]] = ""
      config["COUNTER"] = str(int(config["COUNTER"]) + 1)
    elif position[1] == inputpos[1] and (position[0]+1 == inputpos[0] or position[0]-1 == inputpos[0]):
 #     grid[position[0][position[1]] = grid[inputpos[0]][inputpos[1]]
      grid[position[0]][position[1]] = grid[inputpos[0]][inputpos[1]]
      grid[inputpos[0]][inputpos[1]] = ""
      print("h")
      config["COUNTER"] = str(int(config["COUNTER"]) + 1)
      print(config["COUNTER"])
    else:
      print("No")
  checkwin()

def checkwin():
  checker = []
  for number in range(3):
    for entry in grid[number]:
      checker.append(entry)
  if checker[8] == "":
    checker[8] = 0
    failcount = 0
    for number in range(8):
      if int(checker[number-1]) == int(checker[number]) - 1:
        print("pass")
      else:
        print(int(checker[number-1]), int(checker[number]))
        print("fail")
        failcount = failcount + 1
    if failcount == 0:
      done = True
      print("##########################")
      print("WIN")
      print("##########################")
      done = True
    checker[8] = ""


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (config["WIDTH"] + config["MARGIN"])
            row = pos[1] // (config["HEIGHT"] + config["MARGIN"])
            info = [row,column]
            print("Click ", pos, "Grid coordinates: ", row, column, "Selected Tile: ",grid[row][column])
            acceptmove("Mouse", info)
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            print("Player moved up!")
            acceptmove("Up", "none")
          elif event.key == pygame.K_LEFT:
            print("Player moved left!")
            acceptmove("Left", "none")
          elif event.key == pygame.K_DOWN:
            print("Player moved down!")
            acceptmove("Down", "none")
          elif event.key == pygame.K_RIGHT:
            print("Player moved right!")
            acceptmove("Right", "none")
          elif event.key == pygame.K_r:
            print("Restarting Game!")
            random.shuffle(grid)
            BootUp()

    screen.fill(config["BLACK"])
 

    for row in range(3):
        for column in range(3):
            color = config["WHITE"]
            if grid[row][column] == "":
                color = config["GREEN"]
            pygame.draw.rect(screen, color, [(config["MARGIN"] + config["WIDTH"]) * column + config["MARGIN"], (config["MARGIN"] + config["HEIGHT"]) * row + config["MARGIN"],config["WIDTH"],config["HEIGHT"]])
            text = font.render(str(grid[row][column]), 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.center = ((((config["MARGIN"] + config["WIDTH"]) * column + config["MARGIN"]) + 40),((config["MARGIN"] + config["HEIGHT"]) * row + config["MARGIN"]+40))
            screen.blit(text, textpos)
    countertext = font2.render(("Move Counter:" + config["COUNTER"]), 1, (255, 255, 255))
    screen.blit(countertext, textpos2)

    clock.tick(120)

    pygame.display.flip()


pygame.quit()
