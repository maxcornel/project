def loaddata():

    inputfile1 = open("products","r")
    inputfile2 = open("IDnum", "r")
    inputfile3 = open("beginnumber", "r")
    inputfile4 = open("numbersincategory", "r")

    products = {}
    IDnum = {}
    beginnumber = {}
    numbersincategory = {}

    for line in inputfile1:
        k, v = line.rstrip().split(" ",1)
        products[int(k)] = v

    for line in inputfile2:
        k, v = line.rstrip().split(" ", 1)
        IDnum[k] = int(v)

    for line in inputfile3:
        k, v = line.rstrip().split(" ", 1)
        beginnumber[k] = int(v)

    for line in inputfile4:
        k, v = line.rstrip().split(" ", 1)
        numbersincategory[k] = int(v)



    inputfile1.close()
    inputfile2.close()
    inputfile3.close()
    inputfile4.close()

    return products, IDnum, beginnumber, numbersincategory

print(loaddata())
