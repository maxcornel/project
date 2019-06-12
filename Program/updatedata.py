import Webscraper

def getbeginnum(IDnum):
    IDbegin = {}
    for (k,v) in IDnum.items():
        IDbegin[k] = v+1
    return IDbegin

def numberincat(IDnum,products):                                     #calculate number in categories
    numoftiles = len(products)
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

def updatedata():
    products = Webscraper.getproducts()
    IDnum = Webscraper.getid()
    beginnumber = getbeginnum(IDnum)
    numbersincategory = numberincat(IDnum, products)
    webstyle = Webscraper.getstyle()

    outputfile1 = open("products","w")
    outputfile2 = open("IDnum", "w")
    outputfile3 = open("beginnumber", "w")
    outputfile4 = open("numbersincategory", "w")
    outputfile5 = open("sitepage", "w")

    productskeys = products.keys()
    for key in productskeys:
        nextline = str(key) + " " + products[key]
        outputfile1.write(nextline + "\n")

    IDnumkeys = IDnum.keys()
    for key in IDnumkeys:
        nextline = str(key) + " " + str(IDnum[key])
        outputfile2.write(nextline + "\n")

    beginnumberkeys = beginnumber.keys()
    for key in beginnumberkeys:
        nextline = str(key) + " " + str(beginnumber[key])
        outputfile3.write(nextline + "\n")

    numberincatkeys = numbersincategory.keys()
    for key in numberincatkeys:
        nextline = str(key) + " " + str(numbersincategory[key])
        outputfile4.write(nextline + "\n")

    outputfile5.write("<!doctype html>" +"\n" + "<html>" + "\n" + webstyle)

    outputfile1.close()
    outputfile2.close()
    outputfile3.close()
    outputfile4.close()
    outputfile5.close()

updatedata()

