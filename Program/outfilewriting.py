outfile = open("bonus_lijst.html", "w")                         #open new html file

outfile.write("<!doctype html>" +"\n" + "<html>" + "\n")        #Write HTML file

outfile.write(styleHTML + "\n")

for i in range(3):
    randomnumber = random.randint(0,len(products)-1)
    product = products[randomnumber]
    nextline = str(product.get_attribute("outerHTML"))
    outfile.write(nextline + "\n")

outfile.write("</html>")