def loadproducts():
    products = {}
    with open("products") as inputfile1:
        for line in inputfile1:
            k, v = line.rstrip().split(" ",1)
            products[int(k)] = v
    return products


def loadIDnum():
    IDnum = {}
    with open("IDnum") as inputfile2:
        for line in inputfile2:
            k, v = line.rstrip().split(" ", 1)
            IDnum[k] = int(v)
    return IDnum


def loadbeginnumber():
    beginnumber = {}
    with open("beginnumber") as inputfile3:
        for line in inputfile3:
            k, v = line.rstrip().split(" ", 1)
            beginnumber[k] = int(v)
    return beginnumber


def loadnumbersincategory():
    numbersincategory = {}
    with open("numbersincategory") as inputfile4:
        for line in inputfile4:
            k, v = line.rstrip().split(" ", 1)
            numbersincategory[k] = int(v)
    return numbersincategory







