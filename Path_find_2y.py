import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
fig, ax = plt.subplots(figsize=(10,10))

#https://keesiemeijer.github.io/maze-generator/#generate to generate maze

def to_list(filepath):
  np_array = plt.imread(filepath)
  np_array = np_array[:,:,0]
  np_array = np_array.tolist()

  for i in range(len(np_array)):
    for j in range(len(np_array[0])):
      if np_array[i][j] > 0.5:
        np_array[i][j] = 1
      else:
        np_array[i][j] = 0
  return np_array

lab_list = [[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
],[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]]



def move(direction, start, lab):

  result = []

  if direction == 0:
    result = [start[0] + 1, start[1]]
  elif direction == 1:
    result = [start[0], start[1] - 1]
  elif direction == 2:
    result = [start[0] - 1, start[1]]
  elif direction == 3:
    result = [start[0], start[1] + 1]

  if result[0]>=0 and result[0]<len(lab) and result[1]>=0 and result[1]<len(lab[0]):
    
    if lab[result[0]][result[1]]!=1:

      return result
      
  
  return False

class Facing():

  def __init__(self,direction,max_dir):
    self.max_dir = max_dir
    self.direction = direction

  def increment(self, times, inplace=False):
    
    dir_copy = self.direction


    while times > 0:
      dir_copy += 1
      if dir_copy > self.max_dir:
        dir_copy = 0
      if dir_copy < 0:
        dir_copy = self.max_dir
      times -= 1
    while times < 0:
      dir_copy -= 1
      if dir_copy > self.max_dir:
        dir_copy = 0
      if dir_copy < 0:
        dir_copy = self.max_dir
      times += 1

    if inplace:
      self.direction = dir_copy
      
    return dir_copy
  
  def get(self):
    return self.direction
  
  def set(self, direction):
    self.direction = direction
    return self.direction

def check_surroundings(start, lab):

  result = []

  for i in range(4):
    if move(i, start, lab) != False:
      result.append(True)
    else:
      result.append(False)

  return result

filepath = "prova_3_goal_y_199_x_199.png"

try:
  lab = to_list(filepath)
except:
  lab = lab_list[1]
  print(f"failed to load {filepath}, using default maze")

start = [1,0] #y x

goal = None

for i in range(len(lab)):
  for j in range(len(lab[0])):
    if lab[i][j] == 0.5:
      goal = [i,j]

if goal == None:
  goal = [199, 199] #y x

show_start = True # show at the start

show = True # show the process

showevery = 75


if lab[goal[0]][goal[1]] != 0.5:
  lab[goal[0]][goal[1]] = 0.5

lab[start[0]][start[1]] = 0.7

if show_start:
  plt.imshow(lab)
  plt.show()

facing = Facing(check_surroundings(start, lab).index(True),3) #0 down 1 west 2 up 3 east

found = False

iter = 0

nodes = []

vicolo_cieco = False

shortest_path = [[]]

ims = []

while not found:

  if (check_surroundings(start, lab).count(False) == 2 and iter!=0) or (check_surroundings(start, lab).count(False) == 3 and iter == 0) and not vicolo_cieco:

    for l in [i for i, x in enumerate(check_surroundings(start, lab)) if x == True]:
      if l != facing.increment(2):
        facing.set(l)
        break

    start = move(facing.get(),start,lab)
    
    shortest_path[-1].append(start)

    if lab[start[0]][start[1]] == 0.2:
      vicolo_cieco = True

    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

    lab[start[0]][start[1]] = 0.2  

  elif (check_surroundings(start, lab).count(False) < 2 and not vicolo_cieco) or (check_surroundings(start, lab).count(False) == 2 and iter == 0):
    
    freeways = check_surroundings(start, lab)
    
    if iter != 0:
      freeways[facing.increment(2)] = False

    nodes.append([start,freeways])

    start = move(facing.set(nodes[-1][1].index(True)),start,lab)
    
    shortest_path.append([start])

    if lab[start[0]][start[1]] == 0.2:
      vicolo_cieco = True

    nodes[-1][1][nodes[-1][1].index(True)] = False

    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

    lab[start[0]][start[1]] = 0.2
  
  elif check_surroundings(start, lab).count(False) == 3 or vicolo_cieco:

    shortest_path.pop(-1)

    while nodes[-1][1].count(True) == 0:
      nodes.pop(-1)
    
    start = move(facing.set(nodes[-1][1].index(True)),nodes[-1][0],lab)
    
    shortest_path[-1].append(start)

    nodes[-1][1][nodes[-1][1].index(True)] = False

    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

    lab[start[0]][start[1]] = 0.2

    vicolo_cieco = False
    
  if iter % 1000 == 0:
    print(f"iterazione {iter}")
  
  if iter % showevery == 0:
    lab_copy = [row.copy() for row in lab]
    lab_copy[start[0]][start[1]] = 0.7
    im = ax.imshow(lab_copy, animated=True)
    ims.append([im])

  iter+=1
  if iter>20000:
    break

for i in shortest_path:
  for j in i:
    lab[j[0]][j[1]] = 0.7
  lab_copy = [row.copy() for row in lab]
  im = ax.imshow(lab_copy, animated=True)
  ims.append([im])

for i in range(35):
  ims.append([im])

if found == True:
  print("labirinto risolto in " + str(iter) + " iterazioni")
else:
  print("labirinto non risolto")

plt.imshow(ims[-1][0].get_array())
plt.show()

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save(filename="lab_1.mp4", writer="ffmpeg")
plt.show()