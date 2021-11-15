
from collections import defaultdict

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



