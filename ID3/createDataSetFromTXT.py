def createDataSetFromTXT(filename):
    '''
    创建数据集
    '''
    dataSet = []; labels = [] 
    fr = open(filename)
    linenumber=0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.strip().split()
        lineset = []
        for cel in listFromLine:
            lineset.append(cel)
            
        if(linenumber==0):
            labels=lineset
        else:
            dataSet.append(lineset)
            
        linenumber = linenumber+1
    return dataSet,labels