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

    randomproducten = []
    if meal == "ontbijt":
        randomproducten.append(random.choice(productranges["zuivel-eieren"]))
        randomproducten.append(random.choice(productranges["frisdrank-sappen-koffie-thee"]))
        randomproducten.append(random.choice(productranges["ontbijtgranen-broodbeleg-tussendoor"]))
    elif meal == "lunch":
        randomproducten.append(random.choice(productranges["kaas-vleeswaren-delicatessen"]))
        randomproducten.append(random.choice(productranges["frisdrank-sappen-koffie-thee"]))
        randomproducten.append(random.choice(productranges["bakkerij"]))
    elif meal == "avondeten":
        randomproducten.append(random.choice(productranges["aardappel-groente-fruit"]))
        randomproducten.append(random.choice(productranges["vlees-kip-vis-vega"]))
        randomproducten.append(random.choice(productranges["soepen-conserven-sauzen-smaakmakers"]))
        randomproducten.append(random.choice(productranges["pasta-rijst-internationale-keuken"]))
    elif meal == "borrel":
        randomproducten.append(random.choice(productranges["wijn"]))
        randomproducten.append(random.choice(productranges["bier-sterke-drank-aperitieven"]))
        randomproducten.append(random.choice(productranges["ontbijtgranen-broodbeleg-tussendoor"]))
    elif meal == "snellehap":
        randomproducten.append(random.choice(productranges["verse-kant-en-klaar-maaltijden-salades"]))
        randomproducten.append(random.choice(productranges["frisdrank-sappen-koffie-thee"]))
    elif meal == "snoepen":
        randomproducten.append(random.choice(productranges["snoep-koek-chips"]))

    return randomproducten

