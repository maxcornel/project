import Randomizer
import updatedata
import readdata
import datetime

def getmymeal(meal):
    lastupdate = datetime.date(2019,6,7)
    if lastupdate == datetime.datetime.now():
        updatedata.updatedate()

    randomproducts = Randomizer.randommeal(meal)
    products = readdata.loadproducts()

    for i in randomproducts:
