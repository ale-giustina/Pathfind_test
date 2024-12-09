import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#import some default mazes
import lab_list as ll

#https://keesiemeijer.github.io/maze-generator/#generate to generate maze, the goal is [col*2-1, rows*2-1]

#set the figure size
fig, ax = plt.subplots(figsize=(25,25))

#convert a png file to a list of lists of 0 and 1, the png file must be black and white, walls are white, paths are black
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

#set all the steps to get to a vicolo cieco to 0.3
def block_v(path, lab):
  for i in path:
    lab[i[0]][i[1]] = 0.3
  return lab

#fuse list until it is under x elements
def fuse_list(lab, x):
  while len(lab) > x:
    lab = [lab[0] + lab[1]] + lab[2:]
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

#move in a direction, 0 = down, 1 = left, 2 = up, 3 = right, if the move is possible return the new position, else return False
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

#class to keep track of the direction the algorithm is facing
class Facing():

  def __init__(self,direction,max_dir):
    self.max_dir = max_dir
    self.direction = direction

  #increment direction by times, if inplace is True change the direction of the object, else just return the new direction
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

#check the surroundings of a position, return a list of 4 booleans, True if the direction is possible, False if it's not index 0 = down, 1 = left, 2 = up, 3 = right
def check_surroundings(start, lab):

  result = []

  for i in range(4):
    if move(i, start, lab) != False:
      result.append(True)
    else:
      result.append(False)

  return result



#variables
filename = "maze_209x209_3_goal_417_417"

filepath = f"Mazes/{filename}.png"

start = [1,0] #y x

goal = [417, 417] #y x

#max number of iterations
maxiter = 100000

show = True # show the process

showevery = 120 #show the process every n iterations

showcolor = True #show the process in color

debug = False #show (don't save) the final image



try:
  lab = to_list(filepath)
  print(f"loaded {filepath}")
except:
  lab = ll.get_lab(1)
  print(f"failed to load {filepath}, using default maze")

if goal == None:
  for i in range(len(lab)):
    for j in range(len(lab[0])):
      if lab[i][j] == 0.5:
        goal = [i,j]

if lab[goal[0]][goal[1]] != 0.5:
  lab[goal[0]][goal[1]] = 0.5

lab[start[0]][start[1]] = 0.7

facing = Facing(check_surroundings(start, lab).index(True),3) #0 down 1 west 2 up 3 east

found = False

iter = 0

nodes = []

vicolo_cieco = False

shortest_path = [[]]

ims = []

while not found:


  # if the algo is in a corridor, go straight
  if (check_surroundings(start, lab).count(False) == 3 and iter!=0) or (check_surroundings(start, lab).count(False) == 3 and iter == 0) and not vicolo_cieco:

    #if the algo is in a corridor and the corridor is not straight, turn
    for l in [i for i, x in enumerate(check_surroundings(start, lab)) if x == True]:
      if l != facing.increment(2):
        facing.set(l)
        break

    #move
    start = move(facing.get(),start,lab)
    
    #add move to the shortest path
    shortest_path[-1].append(start)

    #if the algo has run into itself, it's a dead end
    if lab[start[0]][start[1]] == 0.2:
      vicolo_cieco = True

    #if the algo has reached the goal, stop
    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

  #if the algo has more than 1 way to go, add the node to the list of nodes
  elif (check_surroundings(start, lab).count(False) < 3 and not vicolo_cieco) or (check_surroundings(start, lab).count(False) < 3 and iter == 0):
    
    #add the node to the list of nodes [position, [directions] <- True if possible, False if not]
    nodes.append([start,check_surroundings(start, lab)])

    #start going to the first possible direction
    start = move(facing.set(nodes[-1][1].index(True)),start,lab)

    #add the move to the shortest path
    shortest_path.append([start])

    #if the algo has run into itself, it's a dead end
    if lab[start[0]][start[1]] == 0.2:
      vicolo_cieco = True

    #remove possible direction taken from the node
    nodes[-1][1][nodes[-1][1].index(True)] = False

    #if the algo has reached the goal, stop
    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

  #if the algo has nowhere to go, go back to the last node
  elif check_surroundings(start, lab).count(False) == 4 or vicolo_cieco:

    #block the path to the vicolo cieco
    lab = block_v(shortest_path[-1],lab)

    #remove last path from the shortest path
    shortest_path.pop(-1)

    #remove empty nodes until the last node has a possible direction
    while nodes[-1][1].count(True) == 0 or move(facing.set(nodes[-1][1].index(True)),nodes[-1][0],lab)==False:
      nodes.pop(-1)
      lab = block_v(shortest_path[-1],lab)
      shortest_path.pop(-1)
    
    #move to the last node
    start = move(facing.set(nodes[-1][1].index(True)),nodes[-1][0],lab)

    #create a new path
    shortest_path.append([start])

    #remove possible direction taken from the node
    nodes[-1][1][nodes[-1][1].index(True)] = False

    #if the algo has reached the goal, stop
    if lab[start[0]][start[1]] == 0.5:
      lab[start[0]][start[1]] = 0.9
      found = True
      break

    #if the algo has run into itself and has changed direction, remove vicolo cieco flag
    vicolo_cieco = False
  
  #print the iteration every 1000 iterations
  if iter % 1000 == 0:
    print(f"iterazione {iter}")
  
  #show the process
  if (iter % showevery == 0) and show==True:
    #create a copy
    lab_copy = lab.copy()
    #show where the algo is
    lab_copy[start[0]][start[1]] = 0.7
    #if showcolor is True, convert the list to an rgb image
    if showcolor:
      lab_copy = to_rgb(lab_copy)
    #create image
    im = ax.imshow(lab_copy, animated=True)
    ims.append([im])

  #set the position to 0.2 if the algo has been there
  lab[start[0]][start[1]] = 0.2

  iter+=1

  #max_iter check
  if iter>maxiter:
    break


if found == True:
  print("labirinto risolto in " + str(iter) + " iterazioni")

  #fuse the shortest path until it is under 30 elements
  for i in fuse_list(shortest_path, 30):
    
    for j in i:
      lab[j[0]][j[1]] = 0.7
    lab_copy = [row.copy() for row in lab]
    if showcolor:
      lab_copy = to_rgb(lab_copy)
    im = ax.imshow(lab_copy, animated=True)
    ims.append([im])

else:
  print("labirinto non risolto")

#add still frames to the end of the video
lab_copy = [row.copy() for row in lab]
if showcolor:
  lab_copy = to_rgb(lab_copy)
im = ax.imshow(lab_copy, animated=True)
for i in range(60):
  ims.append([im])

print("saving... frames: " + str(len(ims)))

print("saving video...")

#create the animation
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

if debug:
  plt.show()
  plt.close()
else:
  #save the animation
  ani.save(filename=f"Video/{filename}.mp4", writer="ffmpeg")

print("video saved")
print("saving image...")

plt.close(fig)

#close the figure and save the final image
ax, fig = plt.subplots(figsize=(23,23))
im = plt.imshow(lab_copy)
plt.savefig(f"Images/{filename}.png")
