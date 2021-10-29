from io import open_code
from queue import Queue, PriorityQueue
import heapq
from itertools import permutations
import random
import time


def AllStates(): 
    nums = permutations([7,2,4,5,0,6,8,3,1])
    print('Done')

def NewState():

    num = input("Enter State: ")
    action = int(input("Enter Action: (1,2,3,4): ")) 

    state = [int(x) for x in num]

    if action == 1:
        for i in range(0,len(state)-1):
            if state[i] == 0 and i > 2:
                temp = state[i-3]
                state[i-3] = 0
                state[i] = temp
                print (state)
                break

    elif action == 2:
        for i in range(len(state)-1):
            if state[i] == 0 and i < 6:
                temp = state[i+3]
                state[i+3] = 0
                state[i] = temp
                print (state)    
                break

    elif action == 3:
        for i in range(len(state)-1):
            if state[i] == 0 and i != 0 and i != 3 and i != 6:
                temp = state[i-1]
                state[i-1] = 0
                state[i] = temp
                print (state) 
                break

    elif action == 4:
        for i in range(len(state)-1):
            if state[i] == 0 and i != 2 and i != 5 and i != 8:
                temp = state[i+1]
                state[i+1] = 0
                state[i] = temp
                print (state) 
                break

def DivisibleBy3():

    state2 = input("Enter State: ")
    state2 = [int(x) for x in state2]

    num1 = str(state2[0]) + str(state2[1]) + str(state2[2])

    num2 = str(state2[3]) + str(state2[4]) + str(state2[5])

    num3 = str(state2[6]) + str(state2[7]) + str(state2[8])



    while (int(num1) % 3 != 0 or int(num2) % 3 != 0 or int(num3) % 3 != 0):

        action = random.randrange(1,5)

        
        if action == 1:
            for i in range(len(state2)):    
                if state2[i] == 0 and i > 2:
                    temp = state2[i-3]
                    state2[i-3] = 0
                    state2[i] = temp
                    num1 = str(state2[0]) + str(state2[1]) + str(state2[2])
                    num2 = str(state2[3]) + str(state2[4]) + str(state2[5])
                    num3 = str(state2[6]) + str(state2[7]) + str(state2[8])
                    print("State: " + num1 + num2 + num3 + " Action: " + str(action))
                    break
                

        elif action == 2:
            for i in range(len(state2)): 
                if state2[i] == 0 and i < 6:
                    temp = state2[i+3]
                    state2[i+3] = 0
                    state2[i] = temp
                    num1 = str(state2[0]) + str(state2[1]) + str(state2[2])
                    num2 = str(state2[3]) + str(state2[4]) + str(state2[5])
                    num3 = str(state2[6]) + str(state2[7]) + str(state2[8])
                    print("State: " + num1 + num2 + num3 + " Action: " + str(action))
                    break
                

        elif action == 3:
            for i in range(len(state2)): 
                if state2[i] == 0 and i != 0 and i != 3 and i != 6:
                    temp = state2[i-1]
                    state2[i-1] = 0
                    state2[i] = temp
                    num1 = str(state2[0]) + str(state2[1]) + str(state2[2])
                    num2 = str(state2[3]) + str(state2[4]) + str(state2[5])
                    num3 = str(state2[6]) + str(state2[7]) + str(state2[8])
                    print("State: " + num1 + num2 + num3 + " Action: " + str(action))
                    break
                

        elif action == 4:
            for i in range(len(state2)): 
                if state2[i] == 0 and i != 2 and i != 5 and i != 8:
                    temp = state2[i+1]
                    state2[i+1] = 0
                    state2[i] = temp
                    num1 = str(state2[0]) + str(state2[1]) + str(state2[2])
                    num2 = str(state2[3]) + str(state2[4]) + str(state2[5])
                    num3 = str(state2[6]) + str(state2[7]) + str(state2[8])
                    print("State: " + num1 + num2 + num3 + " Action: " + str(action))
                    break
    

    state2 = num1 + num2 + num3

    print(state2)

class StateSetup:
    def __init__(self, state, parent, action, cost):
        
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
    
        if self.state:
                self.states = ''.join(str(i) for i in self.state)



    def __eq__(self, self2):
        return self.states == self2.states

    def __lt__(self, self2):
        return self.states < self2.states

    
    @staticmethod
    def shift(state, action):
    
        global count

        temp = state[:]

        if action == 1:
            for i in range(len(temp)):
                if temp[i] == 0 and i > 2:
                    num = temp[i-3]
                    temp[i-3] = 0
                    temp[i] = num
                    return temp

        elif action == 2:
            for i in range(len(temp)):
                if temp[i] == 0 and i < 6:
                    num = temp[i+3]
                    temp[i+3] = 0
                    temp[i] = num
                    return temp
        
        elif action == 3:
            for i in range(len(temp)):
                if temp[i] == 0 and i != 0 and i != 3 and i != 6:
                    num = temp[i-1]
                    temp[i-1] = 0
                    temp[i] = num
                    return temp
        
        
        elif action == 4: 
            for i in range(len(temp)):
                if temp[i] == 0 and i != 2 and i != 5 and i != 8:
                    num = temp[i+1]
                    temp[i+1] = 0
                    temp[i] = num
                    return temp  
    
            
    def findNodes(self):

        nextPath = []
        nodes=[]

        nextPath.append(StateSetup(self.shift(self.state,1),self.state,'Up',1))
        nextPath.append(StateSetup(self.shift(self.state,2),self.state,'Down',1))
        nextPath.append(StateSetup(self.shift(self.state,3),self.state,'Left',1))
        nextPath.append(StateSetup(self.shift(self.state,4),self.state,'Right',1))

        
        for new in nextPath:
            if(new.state):
                nodes.append(new)
        return nodes


    def findNodesUCS(self):
    
        nextPath = []
        nextPath.append(StateSetup(self.shift(self.state,4),self.state,'Right',0.5))
        nextPath.append(StateSetup(self.shift(self.state,1),self.state,'Up',1))
        nextPath.append(StateSetup(self.shift(self.state,2),self.state,'Down',1))
        nextPath.append(StateSetup(self.shift(self.state,3),self.state,'Left',2))
        

        nodes=[]
        for new in nextPath:
            if(new.state):
                nodes.append(new)  
        return nodes

     

count = 0;


def BFS():

    global count

    initial = [7,2,4,5,0,6,8,3,1]
    goal = [0,1,2,3,4,5,6,7,8]

    start = StateSetup(initial,None,None,0)
    openList = Queue()
    openList.put(start)

    closedList = set()

    while not(openList.empty()):
        node = openList.get()
        closedList.add(node.states)
        paths = node.findNodes()
        for child in paths:
            if child.states not in closedList:
                if child.state == goal:
                    return goal
                openList.put(child)
                count+= 1
                print(str(child.state) + str(child.action))
            

def DFS():
    initial = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    global count

    closedList = set()
    start = StateSetup(initial,None,None,0)
    openList = list()
    openList.append(start)

    while openList:
        node = openList.pop()
        closedList.add(node.states)
        paths = node.findNodes()
        for child in paths:
            if child.states not in closedList:
                if child.state == goal:
                    return goal
                openList.append(child)
                count += 1
                print(str(child.state) + str(child.action))


def clockwise():
    initial = [7,2,4,5,0,6,8,3,1]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    global count

    start = StateSetup(initial,None,None,0)
    openList = Queue()
    openList.put(start)
    closedList = set()

    start = time.time()
    while not(openList.empty()):
        node = openList.get()
        closedList.add(node.states)
        paths = node.findNodes()
        for child in paths:
            if child.states not in closedList: 
                if child.state == goal:
                    return goal
                openList.put(child)
                count += 1
                
        now = time.time()
        if now - start > 180 or count > 500000:
            print("Program took too long...closest state is ...")
            return child.state
    
    

def UCS(option):

   global count
 
   initial = [2,3,4,1,0,8,7,6,5]
   goal = [1,2,3,8,0,4,7,6,5]
 
   start = StateSetup(initial,None,None,0)
   openList = []
   heapq.heappush(openList, start)
   heapq.heapify(openList)
   closedList = set()

   start = time.time()
   while openList:
        node = heapq.heappop(openList)
        if node.state == goal:   
            return goal
        closedList.add(node.states)
        if option == 1:
            paths = node.findNodes()
        elif option == 2:
            paths = node.findNodesUCS()
        for child in paths:
            if child.states not in closedList and child not in openList:
                if child.state == goal:
                    return goal
                heapq.heappush(openList, child)
            elif child in openList:
                for i in range(len(openList)):
                    if  (openList[i].cost > child.cost):
                        openList[i] = child
            count += 1
            print(str(child.state) + str(child.action))   

        now = time.time()
        if now - start > 180:
            print("Program took too long...closest state is ...")
            return child.state   

def main ():
    answer = input("Choose what part of the assignment to solve (a-g): ")

    if answer == 'a':
        AllStates()
    elif answer == 'b':
        NewState()
    elif answer == 'c':
        DivisibleBy3()
    elif answer == 'd':
        goal = BFS()
        print(goal)
        print ("Moves: " +  str(count))
    elif answer == 'e':
        goal = DFS()
        print(goal)
        print ("Moves: " +  str(count))
    elif answer == 'f':
        goal = clockwise()
        print(goal)
        print ("Moves: " +  str(count))
    elif answer == 'g':
        option = int(input ("Choose option 1 or 2: "))
        goal = UCS(option)
        print(goal)
        print ("Moves: " +  str(count))

if __name__ == '__main__':
    main()
