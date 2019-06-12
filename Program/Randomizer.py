import random
import readdata

def randommeal(meal):
    IDnum = readdata.loadIDnum()
    beginnumber = readdata.loadbeginnumber()
    numberincategory = readdata.loadnumbersincategory()
    productranges = {}
    for i in IDnum.keys():
        newlist = list(range(beginnumber[i],beginnumber[i]+numberincategory[i]))
        productranges[i] = newlist

    randomproducts = []
    if meal == "ontbijt":
        randomproducts.append(random.choice(productranges["zuivel-eieren"]))
        randomproducts.append(random.choice(productranges["frisdrank-sappen-koffie-thee"]))
        randomproducts.append(random.choice(productranges["ontbijtgranen-broodbeleg-tussendoor"]))
    elif meal == "lunch":
        randomproducts.append(random.choice(productranges["kaas-vleeswaren-delicatessen"]))
        randomproducts.append(random.choice(productranges["frisdrank-sappen-koffie-thee"]))
        randomproducts.append(random.choice(productranges["bakkerij"]))
    elif meal == "avondeten":
        randomproducts.append(random.choice(productranges["aardappel-groente-fruit"]))
        randomproducts.append(random.choice(productranges["vlees-kip-vis-vega"]))
        randomproducts.append(random.choice(productranges["soepen-conserven-sauzen-smaakmakers"]))
        randomproducts.append(random.choice(productranges["pasta-rijst-internationale-keuken"]))
    elif meal == "borrel":
        randomproducts.append(random.choice(productranges["wijn"]))
        randomproducts.append(random.choice(productranges["bier-sterke-drank-aperitieven"]))
        randomproducts.append(random.choice(productranges["ontbijtgranen-broodbeleg-tussendoor"]))
    elif meal == "snellehap":
        randomproducts.append(random.choice(productranges["verse-kant-en-klaar-maaltijden-salades"]))
        randomproducts.append(random.choice(productranges["frisdrank-sappen-koffie-thee"]))
    elif meal == "snoepen":
        randomproducts.append(random.choice(productranges["snoep-koek-chips"]))

    return randomproducts

def randomalcohol():
    IDnum = readdata.loadIDnum()
    beginnumber = readdata.loadbeginnumber()
    numberincategory = readdata.loadnumbersincategory()
    productranges = {}
    for i in IDnum.keys():
        newlist = list(range(beginnumber[i],beginnumber[i]+numberincategory[i]))
        productranges[i] = newlist

    randomalcohol = []
    randomalcohol = random.choice(productranges["bier-sterke-drank-aperitieven"]+productranges["wijn"])

    return randomalcohol


