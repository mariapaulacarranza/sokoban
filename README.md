# Sokoban Environment - NYU CS-GY6613 - Fall 2020
---
## Prerequisites
Requires python3 to run
##### Install libraries
`$ pip install -r requirements.txt`
## Run the Game

##### Solve as a human
`$ python3 game.py --play`
`$ python3 game.py --agent Human`
##### Solve with an agent
`$ python3 game.py --agent [AGENT-NAME-HERE]`

`$ python3 game.py --agent BFS #run game with BFS agent`

## Parameters
`--play` - run the game as a human player

`--agent [NAME]`  - the type of agent to use [AStar, HillClimber]

`--level [#]` - which level to test (0-99) or 'random' for a randomly selected level that an agent can solve in at most 2000 iterations. These levels can be found in the 'assets/gen_levels/' folder (default=0)

`--iterations [#]` - how many iterations to allow the agent to search for (default=3000)

## Code Functions 
_These are the only functions you need to concern yourselves with to complete the assignments._
**WARNING: DO NOT MODIFY THESE FUNCTIONS!**

#### Sokoban_py
* **state.clone()** - creates a full copy of the current state (for use in initializing Nodes or for feedforward simulation of states without modifying the original) **Use with HillClimber to test sequences**
* **state.checkWin()** - checks if the game has been won in this state _(return type: bool)_
* **state.update(x,y)** - updates the state with the given direction in the form _x,y_ where _x_ is the change in x axis position and _y_ is the change in y axis position. Used to feed-forward a state. **Use with HillClimber Agent to test sequences.**


#### Agent_py
* **Agent()** - base class for the Agents
* **RandomAgent()** - agent that returns list of 20 random directions
* **DoNothingAgent()** - agent that makes no movement for 20 steps

#### Helper_py
* **Other functions**
   * **getHeuristic(state)** - returns the remaining heuristic cost for the current state - a.k.a. distance to win condition (return type: int). **Use with HillClimber Agent to compare states at the end of sequence simulations**
   * **directions** - list of all possible directions (x,y) the agent/player can take **Use with HillClimber Agent to mutate sequences**

* **Node Class**
   * **\_\_init__(state, parent, action)** - where _state_ is the current layout of the game map, _parent_ is the Node object preceding the state, and _action_ is the dictionary XY direction used to reach the state _(return type: Node object)_
   * **checkWin()** - returns if the game is in a win state where all of the goals are covered by crates _(return type: bool)_
   * **getActions()** - returns the sequence of actions taken from the initial node to the current node _(return type: str list)_
   * **getHeuristic()** - returns the remaining heuristic cost for the current state - a.k.a. distance to win condition _(return type: int)_
   * **getHash()** - returns a unique hash for the current game state consisting of the positions of the player, goals, and crates made of a string of integers - for use of keeping track of visited states and comparing Nodes _(return type: str)_
   * **getChildren()** - retrieves the next consecutive Nodes of the current state by expanding all possible directional actions _(return type: Node list)_
   * **getCost()** - returns the depth of the node in the search tree _(return type: int)_

