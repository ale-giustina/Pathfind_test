import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots(figsize=(23,23))

#https://keesiemeijer.github.io/maze-generator/#generate to generate maze, the goal is [col*2-1, rows*2-1]

def to_list(filepath):
  np_array = plt.imread(filepath)
  np_array = np_array[:,:,0]

  for i in range(len(np_array)):
    for j in range(len(np_array[0])):
      if np_array[i][j] > 0.5:
        np_array[i][j] = 1
      else:
        np_array[i][j] = 0

  np_array = np.array(np_array.tolist())
  
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

def block_v(path, lab):
  for i in path:
    lab[i[0]][i[1]] = 0.3
  return lab

#convert to rgb: 1 = black, 0 = white, 0.5 = yellow, 0.7 = green, 0.2 = light_green, 0.3 = light_red

def to_rgb(lab): 
  
  lab = np.array(lab)
  
  result = np.zeros((lab.shape[0],lab.shape[1],3))
  result[lab == 1] = [0,0,0]
  result[lab == 0] = [1,1,1]
  result[lab == 0.5] = [1,1,0]
  result[lab == 0.7] = [0,1,0]
  result[lab == 0.2] = [0,1,0.5]
  result[lab == 0.3] = [1,0,0]
  result[lab == 0.9] = [0,0,1]
  
  return result



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
    
    if lab[result[0]][result[1]]!=1 and lab[result[0]][result[1]]!=0.2 and lab[result[0]][result[1]]!=0.7 and lab[result[0]][result[1]]!=0.3:

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

filename = "maze_208x208_2_goal_415_415"

filepath = f"Mazes/{filename}.png"

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
  goal = [415, 415] #y x

maxiter = 100000

show = True # show the process

showevery = 190

showcolor = True

block_vicoli = True

if lab[goal[0]][goal[1]] != 0.5:
  lab[goal[0]][goal[1]] = 0.5

lab[start[0]][start[1]] = 0.7

facing = Facing(check_surroundings(start, lab).index(True),3) #0 down 1 west 2 up 3 east

found = False

iter = 0

nodes = []

vicolo_cieco = False

debug = False

shortest_path = [[]]

ims = []

while not found:

  if (check_surroundings(start, lab).count(False) == 3 and iter!=0) or (check_surroundings(start, lab).count(False) == 3 and iter == 0) and not vicolo_cieco:

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

  elif (check_surroundings(start, lab).count(False) < 3 and not vicolo_cieco) or (check_surroundings(start, lab).count(False) < 3 and iter == 0):
    
    freeways = check_surroundings(start, lab)
    
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

  elif check_surroundings(start, lab).count(False) == 4 or vicolo_cieco:

    if block_vicoli: lab = block_v(shortest_path[-1],lab)
    shortest_path.pop(-1)

    while nodes[-1][1].count(True) == 0 or move(facing.set(nodes[-1][1].index(True)),nodes[-1][0],lab)==False:
      nodes.pop(-1)
      if block_vicoli: lab = block_v(shortest_path[-1],lab)
      shortest_path.pop(-1)
    
    start = move(facing.set(nodes[-1][1].index(True)),nodes[-1][0],lab)

    shortest_path.append([start])

    nodes[-1][1][nodes[-1][1].index(True)] = False

    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

    vicolo_cieco = False
    
  if iter % 1000 == 0:
    print(f"iterazione {iter}")
  
  if (iter % showevery == 0) and show==True:
    lab_copy = lab.copy()
    lab_copy[start[0]][start[1]] = 0.7
    if showcolor:
      lab_copy = to_rgb(lab_copy)
    im = ax.imshow(lab_copy, animated=True)
    ims.append([im])

  lab[start[0]][start[1]] = 0.2

  iter+=1
  if iter>maxiter:
    break


if found == True:
  print("labirinto risolto in " + str(iter) + " iterazioni")

  for i in shortest_path:
    for j in i:
      lab[j[0]][j[1]] = 0.7
    lab_copy = [row.copy() for row in lab]
    if showcolor:
      lab_copy = to_rgb(lab_copy)
    im = ax.imshow(lab_copy, animated=True)
    ims.append([im])

else:
  print("labirinto non risolto")

lab_copy = [row.copy() for row in lab]
if showcolor:
  lab_copy = to_rgb(lab_copy)
im = ax.imshow(lab_copy, animated=True)
for i in range(60):
  ims.append([im])

print("saving... frames: " + str(len(ims)))

print("saving video...")

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

if debug:
  plt.show()
  plt.close()
else:
  ani.save(filename=f"Video/{filename}.mp4", writer="ffmpeg")

print("video saved")
print("saving image...")

plt.close(fig)

ax, fig = plt.subplots(figsize=(23,23))
im = plt.imshow(lab_copy)
plt.savefig(f"Images/{filename}.png")
