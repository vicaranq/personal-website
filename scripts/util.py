
from collections import defaultdict
import heapq


WEIGHTS_PATH = 'files/weights'

def dotProduct(d1, d2):
    """
    @param dict d1: a feature vector represented by a mapping from a feature (string) to a weight (float).
    @param dict d2: same as d1
    @return float: the dot product between d1 and d2
    """
    if len(d1) < len(d2):
        return dotProduct(d2, d1)
    else:
        return sum(d1.get(f, 0) * v for f, v in list(d2.items()))

def featureExtractor(x):
    # Initialize default int dictionary
    d = defaultdict(int)
    # split string on white spaces
    words_ls = x.split()

    for word in words_ls:
        d[word] += 1
    return d

# Need N-gram feature extractor:
# 
def extractCharFeatures(n):
    def extract(x):
        fv = defaultdict(int)
        x = "".join(x.split()) # splitting string and joining with no space
        if n <= len(x):
            i = 0 
            while i + n <= len(x):
                word_slice = x[i:i+n]
                fv[word_slice] += 1
                i += 1 # move to next char
        return dict(fv)        
    return extract    

def readWeights(path):
    '''
    Reads a set of training examples.
    '''
    w = {}
    c= 0 
    for line in open(path, "rb"):
        # TODO -- change these files to utf-8. latin-1
        line = line.decode('latin-1')
        # Format of each line: <output label (+1 or -1)> <input sentence>
        try:
            key, value = line.split('\t', 1)
        except Exception as e:
            print('the line is: ',line, ' -- ',len(line), ' -- ', line.split(' ', 1))
            raise
        w[key.strip()] = float(value)
        if c < 10:
            print(w)
            c += 1

    print('Read %d weights from %s' % (len(w), path))

    return w

def predict(review):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    # load predictor
    
    weights = readWeights(WEIGHTS_PATH) # sparse vector representing predictor

    #  Phi(x)
    phi = extractCharFeatures(5)
    phi_x = phi(review) # sparse vectore representing features from review

    y = dotProduct(phi_x, weights)

    return 1 if y >= 0 else -1



## WORD SEGMENTATION UTILS

class UniformCostSearch():
    def __init__(self, verbose=0):
        self.verbose = verbose

    def solve(self, problem):
        # If a path exists, set |actions| and |totalCost| accordingly.
        # Otherwise, leave them as None.
        self.actions = None
        self.totalCost = None
        self.numStatesExplored = 0

        # Initialize data structures
        frontier = PriorityQueue()  # Explored states are maintained by the frontier.
        backpointers = {}  # map state to (action, previous state)

        # Add the start state
        startState = problem.startState()
        frontier.update(startState, 0)

        while True:
            # Remove the state from the queue with the lowest pastCost
            # (priority).
            state, pastCost = frontier.removeMin()
            if state == None: break
            self.numStatesExplored += 1
            if self.verbose >= 2:
                print(("Exploring %s with pastCost %s" % (state, pastCost)))

            # Check if we've reached an end state; if so, extract solution.
            if problem.isEnd(state):
                self.actions = []
                while state != startState:
                    action, prevState = backpointers[state]
                    self.actions.append(action)
                    state = prevState
                self.actions.reverse()
                self.totalCost = pastCost
                if self.verbose >= 1:
                    print(("numStatesExplored = %d" % self.numStatesExplored))
                    print(("totalCost = %s" % self.totalCost))
                    print(("actions = %s" % self.actions))
                return

            # Expand from |state| to new successor states,
            # updating the frontier with each newState.
            for action, newState, cost in problem.succAndCost(state):
                if self.verbose >= 3:
                    print(("  Action %s => %s with cost %s + %s" % (action, newState, pastCost, cost)))
                if frontier.update(newState, pastCost + cost):
                    # Found better way to go to |newState|, update backpointer.
                    backpointers[newState] = (action, state)
        if self.verbose >= 1:
            print("No path found")


# Data structure for supporting uniform cost search.
class PriorityQueue:
    def  __init__(self):
        self.DONE = -100000
        self.heap = []
        self.priorities = {}  # Map from state to priority

    # Insert |state| into the heap with priority |newPriority| if
    # |state| isn't in the heap or |newPriority| is smaller than the existing
    # priority.
    # Return whether the priority queue was updated.
    def update(self, state, newPriority):
        oldPriority = self.priorities.get(state)
        if oldPriority == None or newPriority < oldPriority:
            self.priorities[state] = newPriority
            heapq.heappush(self.heap, (newPriority, state))
            return True
        return False

    # Returns (state with minimum priority, priority)
    # or (None, None) if the priority queue is empty.
    def removeMin(self):
        while len(self.heap) > 0:
            priority, state = heapq.heappop(self.heap)
            if self.priorities[state] == self.DONE: continue  # Outdated priority, skip
            self.priorities[state] = self.DONE
            return (state, priority)
        return (None, None)            