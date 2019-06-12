def loadproducts():
    inputfile1 = open("products","r")
    products = {}

    for line in inputfile1:
        k, v = line.rstrip().split(" ",1)
        products[int(k)] = v

    inputfile1.close()

    return products


def loadIDnum():
    inputfile2 = open("IDnum", "r")
    IDnum = {}

    for line in inputfile2:
        k, v = line.rstrip().split(" ", 1)
        IDnum[k] = int(v)

    inputfile2.close()

    return IDnum


def loadbeginnumber():
    inputfile3 = open("beginnumber", "r")
    beginnumber = {}

    for line in inputfile3:
        k, v = line.rstrip().split(" ", 1)
        beginnumber[k] = int(v)

    inputfile3.close()

    return beginnumber


def loadnumbersincategory():
    inputfile4 = open("numbersincategory", "r")
    numbersincategory = {}

    for line in inputfile4:
        k, v = line.rstrip().split(" ", 1)
        numbersincategory[k] = int(v)

    inputfile4.close()

    return numbersincategory









