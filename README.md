# Graph visualisation #

## About ##

The project performs visualisation of Depth-first search (DFS) and Breadth-first search (BFS) algorithms

## Realisation ##

The project was created using the package ```networkx```. You can install a package by adding the package path ```networks``` to PATH

## Example of calling fuctions ##

### Creating graph ###

#### Creating graph from dict ####
``` python
from graph_visualisation.graph import Graph

graph_dict = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph = Graph(dict=graph)
```

#### Creating graph from file ####

``` python
from graph_visualisation.graph import Graph

filename = 'graph.txt'
graph = Graph(filename=filename)
```
Context of graph.txt file

```
A: B, C
B: A
C: A
```
### BFS algorithm ###

``` python
from graph_visualisation.graph import Graph

filename = 'graph.txt'
graph = Graph(filename=filename)
point = 'A'
bfs_vertexes = G.dfs(point)
```
### DFS algorithm ###

``` python
from graph_visualisation.graph import Graph

graph_dict = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph = Graph(dict=graph)
point = 'A'
dfs_vertexes = G.dfs(point)
```
### Create gif of path ###

``` python
from graph_visualisation.graph import Graph

graph_dict = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph = Graph(dict=graph)
point = 'A'
path_dfs = './images_dfs/'
dfs_vertexes = G.dfs(point)
G.draw_graph_path_in_gif(dfs_vertexes, path_dfs)  # path_dfs - directory for saving gif
```

``` python
from graph_visualisation.graph import Graph

filename = 'graph.txt'
graph = Graph(filename=filename)
point = 'A'
path_bfs = './images_dfs/'
bfs_vertexes = G.bfs(point)
G.draw_graph_path_in_gif(bfs_vertexes, path_bfs)  # path_dfs - directory for saving gif
```

## Result ##

At output get a gif file with a visualisation of the graph path

### BFS algorithm ###

![alt text](https://github.com/Drozdova-Daria/graph_lab1/blob/develop/graph_visualisation/images_bfs/graph1.gif)

### DFS algorithm ###

![alt text](https://github.com/Drozdova-Daria/graph_lab1/blob/develop/graph_visualisation/images_dfs/graph1.gif)

## Development team ##

Drozdova Daria

Medvedeva Taya
