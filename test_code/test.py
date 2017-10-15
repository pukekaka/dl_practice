






'''
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