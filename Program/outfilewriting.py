import Randomizer
import readdata
import webbrowser, os

def getmymeal(meal): #meals are ontbijt, lunch, avondeten, borrel, snellehap, snoepen
    outputfile6 = open("sitepage.html", "w")
    randomproducts = Randomizer.randommeal(meal)
    products = readdata.loadproducts()

    with open("style") as stylepage:
        sitestyle = stylepage.read()
        outputfile6.write(sitestyle + "\n")

    for i in randomproducts:
        product = products[i]
        nextline = str(product)
        outputfile6.write(nextline + "\n")

    outputfile6.write("</html>")
    outputfile6.close()
    webbrowser.open('file://' + os.path.realpath("sitepage.html"))

getmymeal("avondeten")


