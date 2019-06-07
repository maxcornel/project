import Webscraper


def getbeginnum(IDnum):
    IDbegin = {}
    for (k,v) in IDnum.items():
        IDbegin[k] = v+1
    return IDbegin

def numberincat(IDnum):
    numoftiles = len(Webscraper.getproducts())
    listofplace = list(IDnum.values())
    numincat = []
    for i in range(len(listofplace)-1):
        nextnum = listofplace[i+1] - listofplace[i]
        numincat.append(nextnum)
    lastnum = numoftiles - listofplace[len(listofplace)-1]
    numincat.append(lastnum)
    return numincat

'''def getendnum(IDnum):
    IDend = {}
    for (k,v)
'''
IDnum = Webscraper.getid()
print(numberincat(IDnum))



