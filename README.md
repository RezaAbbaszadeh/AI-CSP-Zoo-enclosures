# Zoo enclosures CSP
The problem gives the number of enclosures with their adjacencies and a list of animals and ask us to plan where each animal goes.<br>
There are 2 constraints:
- Enclosure must be larger than animal inside it
- Some animals can not be placed in adjacency of another animals

### Input
In first line N,P,M are given which are number of cages, number of animals, number of adjacencies between enclosures.<br>
Second line gives size of enclosures and Third line gives size of animals.<br>
In next M lines the enclosures that are adjacent to each other are given.<br>
In next P Lines a P*P matrix is given that shows which animals can be in adjacent enclosures.

```
18 18 22
5 2 3 4 4 3 5 2 4 3 3 2 4 3 1 4 5 2
4 1 3 1 2 1 5 4 3 2 3 2 2 4 5 3 2 4
1 2
2 3
2 4
4 5
4 6
1 8
4 7
7 8
8 9
9 10
9 11
10 5
6 9
6 11
11 12
12 13
13 14
14 15
15 16
16 17
17 18
17 1
1 0 1 0 0 1 1 1 0 0 0 1 0 0 0 1 0 1
0 1 1 1 0 0 0 0 1 1 1 0 1 0 0 0 0 0
1 1 1 0 0 0 0 0 0 1 1 0 1 1 1 0 0 1
0 1 0 1 0 1 0 0 0 0 1 0 0 0 0 0 1 0
0 0 0 0 0 1 1 1 0 0 1 0 1 0 1 0 0 0
1 0 0 1 1 0 0 1 0 0 1 1 0 0 0 1 1 0
1 0 0 0 1 0 1 1 0 0 0 1 1 1 0 0 1 1
1 0 0 0 1 1 1 1 0 0 0 0 1 1 1 0 0 0
0 1 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0
0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1
0 1 1 1 1 1 0 0 0 1 0 1 0 0 0 1 1 1
1 0 0 0 0 1 1 0 0 1 1 1 0 0 1 0 0 1
0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 0 1 1
0 0 1 0 0 0 1 1 0 0 0 0 1 0 0 0 1 1
0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 0 0 0
1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 1
0 0 0 1 0 1 1 0 0 0 1 0 1 1 0 1 0 1
1 0 1 0 0 0 1 0 0 1 1 1 1 1 0 1 1 0
```

### Output
possible arrangements of animals in enclosures.<br>
Each line contains all enclosures ordered as given in input and the index of animal inside it
```
3 possible outputs for above input
1: [[7], [5], [3], [11], [0], [9], [6], [12], [17], [15], [10], [16], [13], [2], [1], [8], [14], [4]]
2: [[7], [5], [3], [0], [11], [15], [6], [12], [17], [9], [10], [16], [13], [2], [1], [8], [14], [4]]
3: [[7], [5], [3], [0], [17], [15], [6], [4], [10], [9], [16], [12], [13], [2], [1], [8], [14], [11]]
```
