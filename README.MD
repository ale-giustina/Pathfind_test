# Pathfinding test with visual representation

This is a simple pathfinding test using the both "keep the right" algorithm and the depth-first search algorithm.

The maze is represented by a png, the white pixels are walls and the black pixels are paths.

Almost all the mazes were generated with Kees Meijer maze generator found at https://keesiemeijer.github.io/maze-generator/.

## Maze examples

### Fully connected maze without removing walls

<img alt="Maze 3" src="Mazes/prove/prova_3_goal_y_199_x_199.png" width=400> <img alt="Maze 3 solved" src="Mazes/prove/maze-solved-3.png" width=400>

<img alt="Maze 4" src="Mazes/prove/prova_4_goal_y_99_x_99.png" width=400> <img alt="Maze 4 solved" src="Mazes/prove/maze-solved-4.png" width=400>

### Maze with removed walls

<img alt="Maze 5" src="Mazes\Wout_walls\maze_20x20_wout_walls_goal_39_39.png" width=400> <img alt="Maze 5 solved" src="Mazes\Wout_walls\maze-solved_20x20_wout_walls.png" width=400>


## Example output

### Fully connected maze without removing walls
<img alt="Maze 6" src="Images\GIFS\prova_4_goal_y_99_x_99.gif" width=400> <img alt="Maze 6 solved" src="Mazes\prove\maze-solved-4.png" width=400>

<img alt="Maze 8" src="Images\GIFS\maze_208x208_2_goal_415_415.gif" width=400> <img alt="Maze 8 solved" src="Mazes\maze-solved_208x208_2.png" width=400>

<img alt="Maze 9" src="Images\GIFS\maze_209x209_3_goal_417_417.gif" width=400> <img alt="Maze 9 solved" src="Mazes\maze-solved_209x209_3.png" width=400>

<img alt="Maze 10" src="Images\GIFS\maze_209x209_4_goal_417_417.gif" width=400> <img alt="Maze 10 solved" src="Mazes\maze-solved_209x209_4.png" width=400>



### Maze with removed walls
<img alt="Maze 7" src="Images\GIFS\maze_20x20_wout_walls_goal_39_39.gif" width=400> <img alt="Maze 7 solved" src="Mazes\Wout_walls\maze-solved_20x20_wout_walls.png" width=400>

# example with goal in the center
<img alt="Maze 8" src="Images\GIFS\maze_50x50_minus_300_walls.gif" width=400>

## How to run
In the Path_find_depth_first.py and Path_find_keep_right.py files you can change the filename or specify a given list with a start and a goal. The interval between snapshots can also be changed.

## Requirements
- Python 3 (3.10.1 used)
- Numpy
- matplotlib
- FFmpeg (for video creation)
