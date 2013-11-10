import csv
 
def addDollarSign(amt):
    if amt[0] == '$':
        return amt
    else:
        return '$'+amt

def handleLatexChars(s):
    return s.replace("$","\\$").replace("&","\\&").replace("#","\\#").replace("^","\\^")

sample = open('FinalSilentAuction.csv', "rb")
readSample = csv.reader(sample)
 
f = open('servsheets.tex','w')
 
print >>f, "\documentclass[11pt]{article}"
print >>f, "\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>f, "\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>f, "\setlength{\parindent}{0in}"
print >>f, "\\begin{document}"

categories = [[],[],[],[],[],[],[]]
 
for item in readSample:
    if (item[5] == "Business Donations"):
        categories[0].append(item)
    elif (item[5] == "Arts and Crafts"):
        categories[1].append(item)
    elif (item[5] == "Events"):
        categories[2].append(item)
    elif (item[5] == "Food"):
        categories[3].append(item)
    elif (item[5] == "Lessons"):
        categories[4].append(item)
    elif (item[5] == "Services"):
        categories[5].append(item)
    elif (item[5] == "Miscellaneous"):
        categories[6].append(item)

for (i,category) in enumerate(categories): 
    category = sorted(category,key=lambda item: float(item[3].lstrip('$'))) # sort by minimum bid, lowest to highest
    for (j,item) in enumerate(category):
        print >>f, "\section*{"+str(i+1)+"."+str(j+1)+" "+handleLatexChars(item[2])+"}" # title
        print >>f, handleLatexChars(item[0]) # name
        print >>f, "\\\\"
        print >>f, "Starting Bid: "+handleLatexChars(addDollarSign(item[3]))
        print >>f, "\\newline"
        print >>f, handleLatexChars(item[4]).rstrip() # description
        print >>f, "\\\\[3ex]"
        print >>f, "\\begin{tabular}{c c c}"
        print >>f, "~~~~~~~~~~~~~Name~~~~~~~~~~~~~ & ~~~~~~~~~Bid (\$)~~~~~~~~~  & ~~~Email Address (if not standard olin.edu)~~~\\"+"\\"
        for a in range(19): # print lines for bids
            print >>f, " & & \\"+"\\"
            print >>f, "\hline"
        print >>f, "\\end{tabular}"
        print >>f, "\\newpage"

print >>f, "\\end{document}"