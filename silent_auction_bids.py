import csv
 
def addDollarSign(amt):
    if amt[0] == '$':
        return amt
    else:
        return '$'+amt

def handleLatexChars(s):
    return s.replace("$","\\$").replace("&","\\&").replace("#","\\#").replace("^","\\^")

sample = open('2013/FinalSilentAuction.csv', "rb")
readSample = csv.reader(sample)
 
f = open('2013/servsheets.tex','w')
g = open('2013/servpacket.tex','w')

print >>f, "\\documentclass[11pt]{article}"
print >>f, "\\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>f, "\\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>f, "\\setlength{\parindent}{0in}"
print >>f, "\\begin{document}"

print >>g, "\\documentclass[11pt]{article}"
print >>g, "\\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>g, "\\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>g, "\\setlength{\parindent}{0in}"
print >>g, "\\title{Silent Auction Donation Packet}"
print >>g, "\\author{SERV Auction 2013}"
print >>g, "\\date{November 11th, 2013 to November 15th, 2013}"
print >>g, "\\begin{document}"
print >>g, "\\maketitle"

categories = [[],[],[],[],[],[],[]]
categoryNames = ["Business Donations","Arts and Crafts","Events","Food","Lessons","Services","Miscellaneous"]
 
for item in readSample:
    if (item[5] == categoryNames[0]):
        categories[0].append(item)
    elif (item[5] == categoryNames[1]):
        categories[1].append(item)
    elif (item[5] == categoryNames[2]):
        categories[2].append(item)
    elif (item[5] == categoryNames[3]):
        categories[3].append(item)
    elif (item[5] == categoryNames[4]):
        categories[4].append(item)
    elif (item[5] == categoryNames[5]):
        categories[5].append(item)
    elif (item[5] == categoryNames[6]):
        categories[6].append(item)

for (i,category) in enumerate(categories): 
    category = sorted(category,key=lambda item: float(item[3].lstrip('$'))) # sort by minimum bid, lowest to highest
    print >>g, "\section{"+categoryNames[i]+"}"
    for (j,item) in enumerate(category):
        print >>f, "\section*{"+str(i+1)+"."+str(j+1)+" "+handleLatexChars(item[2])+"}" # title
        print >>f, handleLatexChars(item[0]) # name
        print >>f, "\\\\"
        print >>f, "Starting Bid: "+handleLatexChars(addDollarSign(item[3]))
        print >>f, "\\newline"
        print >>f, handleLatexChars(item[4]).rstrip() # description
        print >>f, "\\\\[6ex]"
        print >>f, "\\begin{tabular}{c c c}"
        print >>f, "~~~~~~~~~~~~~Name~~~~~~~~~~~~~ & ~~~~~~~~~Bid (\$)~~~~~~~~~  & ~~~Email Address (if not standard olin.edu)~~~\\"+"\\"
        for a in range(26): # print lines for bids
            print >>f, " & & \\"+"\\"
            print >>f, "\hline"
        print >>f, "\\end{tabular}"
        print >>f, "\\newpage"

        print >>g, "\subsection{"+handleLatexChars(item[2])+"}" # title
        print >>g, handleLatexChars(item[0]) # name
        print >>g, "\\\\"
        print >>g, "Starting Bid: "+handleLatexChars(addDollarSign(item[3]))
        print >>g, "\\newline"
        print >>g, handleLatexChars(item[4]).rstrip() # description

print >>f, "\\end{document}"
print >>g, "\\end{document}"