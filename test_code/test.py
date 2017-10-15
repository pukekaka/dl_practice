

'''
def make_forge():
    X, y = make_blobs(centers=2, random_state=4, n_samples=30)
        y[np.array([7, 27])] = 0
        mask = np.ones(len(X), dtype=np.bool)
        mask[np.array([0, 1, 5, 26])] = 0
        X, y = X[mask], y[mask]
        return X, y



numFeat = len(open("abalone.txt").readline().split('\t')) - 1
dataMat = []; labelMat = []
fr = open("abalone.txt")
print (numFeat)
for line in fr.readlines():
    lineArr = []
    curLine = line.strip().split('\t')
    for i in range(numFeat):
        lineArr.append(float(curLine[i]))
        #print (lineArr)
    dataMat.append(lineArr)
    labelMat.append(float(curLine[-1]))
    print(dataMat)
    #print(labelMat)
    
    
    
        
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
'''