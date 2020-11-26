# SOLVER CLASSES WHERE AGENT CODES GO
from helper import *
import random



# Base class of agent (DO NOT TOUCH!)
class Agent:
    def getSolution(self, state, maxIterations):
        return []       # set of actions


#####       EXAMPLE AGENTS      #####

# Do Nothing Agent code - the laziest of the agents
class DoNothingAgent(Agent):
    def getSolution(self, state, maxIterations):
        if maxIterations == -1:     # RIP your machine if you remove this block
            return []

        #make idle action set
        nothActionSet = []
        for i in range(20):
            nothActionSet.append({"x":0,"y":0})

        return nothActionSet

# Random Agent code - completes random actions
class RandomAgent(Agent):
    def getSolution(self, state, maxIterations):

        #make random action set
        randActionSet = []
        for i in range(20):
            randActionSet.append(random.choice(directions))

        return randActionSet




#####    ASSIGNMENT 1 AGENTS    #####

dirX = [-1,1,0,0]
dirY = [0,0,-1,1]
# BFS Agent code
class BFSAgent(Agent):
class BFSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        min_heuristic = 99999999999999
        # YOUR CODE HERE
        queue = []
        visited=set()
        st = Node(state = state,parent = None,action=None)
        start_state = state
        queue.append(st)
        
        while (queue and (iterations<maxIterations or maxIterations<=0)):
            curr_node = queue[0]
            queue.pop(0)
            
            curr_state = curr_node.state
            if(checkDeadlock(curr_state)):
                continue
            arr = []
            for crate in curr_state.crates:
                arr.append((crate['x'],crate['y']))
            curr_state_values = tuple((curr_state.player['x'],curr_state.player['y'],tuple(arr)))
            if(curr_state_values in visited):
                continue
            iterations+=1
            visited.add(curr_state_values)
            dist = curr_node.getHeuristic()
            if(dist==0):
                bestNode = curr_node
                break
            if(dist<min_heuristic):
                min_heuristic = dist
                bestNode = curr_node
            for i in range(4):
                newState = curr_state.clone()
                newState.update(dirX[i],dirY[i])
                
                newNode = Node(state=newState,parent=curr_node,action = directions[i]);
                queue.append(newNode)

        #return []                       #remove me
        return bestNode.getActions() or []   #uncomment me



# DFS Agent Code
class DFSAgent(Agent):
    def dfsUtil(self, curr_node, visited, iterationsLeft,bestNode,min_heuristic):
        if(iterationsLeft<=0):
            return iterationsLeft
        if(min_heuristic[0]==0):
            return iterationsLeft
        iterationsLeft-=1
        curr_state = curr_node.state
        arr = []
        for crate in curr_state.crates:
            arr.append((crate['x'],crate['y']))
        curr_state_values = tuple((curr_state.player['x'],curr_state.player['y'],tuple(arr)))
        print(curr_state_values)
        if(curr_state_values in visited):
            return iterationsLeft
        #print(visited)
        visited.add(curr_state_values)
        if(checkDeadlock(curr_state)):
            return iterationsLeft
        dist = curr_node.getHeuristic()
        if(min_heuristic[0]>dist):
            print("work")
            min_heuristic[0] = dist
            if(len(bestNode)):
                bestNode.pop()
            bestNode.append(curr_node)
        if dist == 0:
            return iterationsLeft
        for i in range(4):
            newState = curr_state.clone()
            newState.update(dirX[i],dirY[i])
            newNode = Node(state=newState,parent=curr_node,action = directions[i]);
            iterationsLeft = self.dfsUtil(newNode,visited,iterationsLeft,bestNode,min_heuristic)
        return iterationsLeft
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = []
        if(maxIterations==-1):
            maxIterations=math.inf
        # YOUR CODE HERE
        visited = set()
        min_heuristic = [math.inf]
        st = Node(state = state,parent = None,action=None)
        self.dfsUtil(st,visited,maxIterations,bestNode,min_heuristic)



        #return []                       #remove me
        #print(bestNode[0].parent)
        return bestNode[0].getActions() or []   #uncomment me




#####    ASSIGNMENT 2 AGENTS    #####



# AStar Agent Code
class AStarAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        balance = 1
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        Node.balance = balance
        min_heuristic = 99999999999999999999999999
        #initialize priority queue
        queue = PriorityQueue()
        queue.put((100,Node(state.clone(), None, None)))
        visited = set()

        while (iterations < maxIterations or maxIterations <= 0) and queue.qsize() > 0:
            iterations += 1
            print("fssfgs")
            ## YOUR CODE HERE ##
            curr_val = queue.get()
            curr_node = curr_val[1]
            curr_state = curr_node.state
            if(checkDeadlock(curr_state)):
                continue
            arr = []
            for crate in curr_state.crates:
            	arr.append((crate['x'],crate['y']))
            curr_state_values = tuple((curr_state.player['x'],curr_state.player['y'],tuple(arr)))
            if(curr_state_values in visited):
            	continue
            iterations+=1
            visited.add(curr_state_values)
            dist = curr_node.getHeuristic()
            if(dist==0):
            	bestNode = curr_node
            	break
            if(dist<min_heuristic):
            	min_heuristic = dist
            	bestNode = curr_node
            for i in range(4):
            	newState = curr_state.clone()
            	newState.update(dirX[i],dirY[i])            	
            	newNode = Node(state=newState,parent=curr_node,action = directions[i]);
            	queue.put((newNode.getHeuristic()+newNode.getCost(),newNode))

        return bestNode.getActions()


# Hill Climber Agent code
class HillClimberAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        
        seqLen = 50            # maximum length of the sequences generated
        coinFlip = 0.5          # chance to mutate

        #initialize the first sequence (random movements)
        bestSeq = []
        for i in range(seqLen):
            bestSeq.append(random.choice(directions))
        
        #Global Variables Required
        start_node = Node(state,None,None)
        last_node = start_node
        min_heuristic = 99999999999999
        currSeq = bestSeq[:]
        #mutate the best sequence until the iterations runs out or a solution sequence is found
        while (iterations < maxIterations or maxIterations<=0):
            iterations += 1
            
            ## YOUR CODE HERE ##

            initialIter = True
            for i in range(seqLen):
            	if initialIter:
            		currSeq[i] = random.choice(directions)
            		initialIter = False
            	else:
            		if(random.random()>=coinFlip):
            			currSeq[i] = random.choice(directions)
            
            curr_state = state.clone()
            deadlock = False
            for i in range(seqLen):
            	curr_state.update(currSeq[i]['x'],currSeq[i]['y'])
            	if(curr_state.checkWin()):
            		bestSeq = currSeq
            		return bestSeq[:i+1]
            	if(checkDeadlock(curr_state)):
            		deadlock = True
            		break
            	
            if deadlock:
            	continue
            dist = getHeuristic(curr_state)
            if dist<min_heuristic:
            	min_heuristic = dist
            	bestSeq = currSeq
        #return the best sequence found
        return bestSeq  



#####    ASSIGNMENT 3 AGENTS    #####

# Genetic Algorithm code
class GeneticAgent(Agent):
    def pairSelect(self):
        x=random.randint(1,36)
        y=random.randint(1,36)
        
        x = self.calculateProbability(x)
        y = self.calculateProbability(y)
        ''' Here we go on selecting y until it differs from x.
        This is done in order to avoid same X and Y chromosome'''
        while x==y:
            y=random.randint(1,36)
            y = self.calculateProbability(y)
            
        return x,y
    
    def calculateProbability(self,number):
        
        if number==1:
            return 7
        elif number<=3:
            return 6
        elif number <=6:
            return 5
        elif number<=10:
            return 4
        elif number <=15:
            return 3
        elif number<=21:
            return 2
        elif number <=28:
            return 1
        elif number<=36:
            return 0
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        populationList = []
        curr_node = Node(state,None,None)
        popSize = 50
        seqSize = 50
        min_heuristic = -math.inf
        for i in range(popSize):
            list1 = []
            for j in range(seqSize):
                list1.append(random.choice(directions))
            populationList.append(list1)
        # YOUR CODE HERE
        while(iterations<maxIterations):
            iterations+=1
            curr_population = []
            for i in range(popSize):
                tempState = state.clone()
                for j in range(seqSize):
                    tempState.update(populationList[i][j]['x'],populationList[i][j]['y'])
                    if(checkDeadlock(tempState)):
                        break
                    if(tempState.checkWin()):
                        return populationList[i][:j+1]
                curr_population.append((populationList[i][:],getHeuristic(tempState)))

            curr_population.sort(key = lambda x:x[1],)
            if curr_population[0][1]>min_heuristic:
                min_heuristic = curr_population[0][1]
                bestNode = curr_population[0][0][:]

            populationList = []
            # s = int((10*popSize)/100)
            # for i in range(s):
            #     populationList.append(curr_population[i][0])
            for i in range(popSize//2):
                rank1,rank2 = self.pairSelect()
                x_chromosome = curr_population[rank1][0][:]
                y_chromosome = curr_population[rank2][0][:]
                crossover = random.randint(0,100)

                if random.random()<=0.7:
                    child1 = []
                    child2 = []
                    for j in range(seqSize):
                        if random.random()>=0.5:
                            child1.append(x_chromosome[j])
                            child2.append(y_chromosome[j])
                        else:
                            child1.append(y_chromosome[j])
                            child2.append(x_chromosome[j])
                    populationList.append(child1)
                    populationList.append(child2)
                else:
                    populationList.append(x_chromosome[:])
                    populationList.append(y_chromosome[:])

            for i in range(popSize):
                if random.random()<=0.1:
                    
                    populationList[i][random.randint(0,popSize//2)] = random.choice(directions)


        #return []                     #remove me
        print(bestNode)
        return bestNode   #uncomment me


# Monte Carlo Tree Search Algorithm code

class MCTSAgent(Agent):
    
    def backpropogate(self,curr_node,reward):
        curr_node.visits+=1
        curr_node.reward+=reward
        if curr_node.parent != None:
            self.backpropogate(curr_node.parent,reward)
    def rollout(self,curr_node):
        curr_state = curr_node.state
        val = -10
        while(1):
            if(curr_state.checkWin()):
                val = 10
                break
            if(checkDeadlock(curr_state)):
                break
            next_action = random.choice(directions)
            curr_state.update(next_action['x'],next_action['y'])
        return val
    def best_child(self,curr_node, c_param = 1.4):
        children = curr_node.children
        # choices_weights = [
        #     ((c.reward / c.visits) + c_param * math.sqrt(2.0*math.log(curr_node.visits)/float(c.visits)))
        #     for c in children
        # ]
        bestChild = []
        currmax = -math.inf
        for c in children:
            result = ((c.reward / c.visits) + c_param * math.sqrt(2.0*math.log(curr_node.visits)/float(c.visits)))
            if result==currmax:
                bestChild.append(c)
            if(result>currmax):
                currmax = result
                bestChild = [c]
        return random.choice(bestChild)

    def expand(self,curr_node):
        self.cnt+=1
        if(curr_node.actions_left <=0):
            return (curr_node,False)
        next_action = directions[curr_node.actions_left-1]
        curr_node.actions_left -= 1
        curr_state = curr_node.state
        
        child_state = curr_state.clone()
        child_state.update(next_action['x'],next_action['y'])
        if(curr_node.parent!=None):
            if(child_state == curr_node.parent.state):
                return (curr_node,False)
        child_node = Node(child_state,curr_node,next_action)
        curr_node.children.append(child_node)
        return child_node,True

    def traverse(self,curr_node):
        curr_state = curr_node.state
        while(1):
            print("w")
            if(checkDeadlock(curr_state)):
                self.dead+=1
                break
            if(curr_node.actions_left>0):
                terminal_node,check = self.expand(curr_node)
                if check == False:
                    continue
                return terminal_node
            child_node = self.best_child(curr_node)
            curr_node = child_node
            curr_state = curr_node.state

        return curr_node

    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        self.cnt = 0
        self.dead = 0
        self.visited = set()
        bestNode = None
        start_node = Node(state,None,None)
        min_heuristic = math.inf
        # YOUR CODE HERE
        while(iterations<maxIterations):
            iterations+=1
            print("Complete")
            curr_node = self.traverse(start_node)
            curr_reward = self.rollout(curr_node)
            print(curr_reward)
            self.backpropogate(curr_node,curr_reward)
            print(curr_node)
            dist = curr_node.getHeuristic()
            
            if(dist<min_heuristic):
                min_heuristic=dist
                bestNode = curr_node

        #return []                     #remove me
        print(bestNode)
        print("cnt ",self.cnt)
        print("dead ",self.dead)
        return bestNode.getActions()   #uncomment me

