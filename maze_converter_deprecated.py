#https://keesiemeijer.github.io/maze-generator/#generate to generate maze
import numpy as np
import matplotlib.pyplot as plt

#load image and given numbers of rows and columns take the maze and convert it to a list the maze is a png image and its size is invariant

def to_list(filepath):
  np_array = plt.imread(filepath)
  np_array = np_array[:,:,0]
  np_array = np_array.tolist()
  for i in range(len(np_array)):
    np_array[i] = np_array[i][::-1]
  return np_array

rows = 20 * 2
columns = 20 * 2

final_list = []
img_list = to_list('maze.png')

plt.imshow(img_list, cmap='gray')
plt.show()

left_edge = len(img_list[0]) // rows
top_edge = len(img_list) // columns

first_center = [top_edge // 2, left_edge // 2]

for i in range(rows+1):
  row = []
  for j in range(columns+1):
    print([first_center[0] + i * top_edge,first_center[1] + j * left_edge])
    row.append((img_list[first_center[0] + i * top_edge][first_center[1] + j * left_edge]-1)*-1)
  final_list.append(row[::-1])



plt.imshow(final_list, cmap='gray')
plt.show()
plt.imsave('prova_1.png', final_list, cmap='gray')