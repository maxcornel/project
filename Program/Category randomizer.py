import Webscraper


def getbeginnum(IDnum):
    IDbegin = {}
    for (k,v) in IDnum.items():
        IDbegin[k] = v+1
    return IDbegin

def numberincat(IDnum):                                     #calculate number in categories
    numoftiles = len(Webscraper.getproducts())
    listofplace = list(IDnum.values())
    listofID = list(IDnum.keys())
    listofsize = []
    for i in range(len(listofplace)-1):
        nextnum = listofplace[i+1] - listofplace[i] - 1
        listofsize.append(nextnum)
    lastnum = numoftiles - listofplace[len(listofplace)-1]
    listofsize.append(lastnum)

    numincat = {}
    for i in range(len(listofID)):
        numincat[listofID[i]] = listofsize[i]

    return numincat

'''def getendnum(IDnum):
    IDend = {}
    for (k,v)
'''
IDnum = Webscraper.getid()
print(numberincat(IDnum))



