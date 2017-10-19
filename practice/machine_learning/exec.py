import practice.machine_learning.modules.trees as trees


if __name__ == "__main__":
    myData, labels = trees.createDataset()
    print('Data:', myData)

    #myData[0][-1] = 'maybe'
    #print('2. Data Change:', myData)

    entropy = trees.calcEntropy(myData)
    print('entropy:', entropy)

    retData = trees.splitDataset(myData, 0, 1)
    print(retData)