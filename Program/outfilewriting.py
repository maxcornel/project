import Randomizer
import updatedata
import readdata
import datetime



def getmymeal(meal):
    outputfile5 = open("sitepage", "w")
    lastupdate = datetime.date(2019,6,7)
    if lastupdate == datetime.datetime.now():
        updatedata.updatedate()

    randomproducts = Randomizer.randommeal(meal)
    products = readdata.loadproducts()

    for i in randomproducts:
        product = products[i]
        nextline = str(product)
        outputfile5.write(nextline + "\n")

    outputfile5.write("</html>")
    outputfile5.close()

getmymeal("ontbijt")