# KNOWN ANOMALIES: "\^\^" is not valid Latex (needs to not be escaped), but "^" must be escaped everywhere else. Odd edge case.

import csv
from helpers import *

sample = open('2016/silent.csv', "rb")
readSample = csv.reader(sample, delimiter=',', quotechar='"')

f = open('2016/servsheets.tex','w')
g = open('2016/servpacket.tex','w')

print >>f, "\\documentclass[11pt]{article}"
print >>f, "\\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>f, "\\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>f, "\\setlength{\parindent}{0in}"
print >>f, "\\begin{document}"

print >>g, "\\documentclass[11pt]{article}"
print >>g, "\\pagestyle{plain} \\topmargin -.5in \oddsidem argin 0in"
print >>g, "\\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>g, "\\setlength{\parindent}{0in}"
print >>g, "\\title{Silent Auction Donation Packet}"
print >>g, "\\author{SERV Auction 2016}"
# TODO: Update these dates.
print >>g, "\\date{November 7th, 2016 to November 11th, 2016}"
print >>g, "\\begin{document}"
print >>g, "\\maketitle"

categories = [[],[],[],[],[],[]]
categoryNames = ["Services", "Food", "Events", "Lessons", "Arts and Crafts", "Miscellaneous"]

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

for (i, category) in enumerate(categories):

    category = sorted(category,key=lambda item: float(item[8].lstrip('$').rstrip('$'))) # sort by minimum bid, lowest to highest
    print >>g, "\section{"+categoryNames[i]+"}"
    for (j,item) in enumerate(category):

        # NOTE: Change the numbers here to match the CSV.
        # timestamp   = item[0]
        personName  = item[1]
        email       = item[2]
        # affiliation = item[3]
        title       = item[4]
        # category    = item[5]
        # interestFor = item[6]
        # isForLive   = item[7]
        startingBid = item[8]
        description = item[9]
        numWinners  = item[10]

        print >>f, "\section*{"+str(i+1)+"."+str(j+1)+" "+handleLatexChars(title)+"}" # title
        print >>f, handleLatexChars(personName) # name
        print >>f, "\\\\"
        print >>f, "Starting Bid: "+handleLatexChars(addDollarSign(startingBid))
        print >>f, "\\newline"
        if (numWinners != '' and handleLatexChars(numWinners) != '1'):
            print >>f, "Number of winners: "+handleLatexChars(numWinners)
            print >>f, "\\newline"
        print >>f, handleLatexChars(description).rstrip() # description
        print >>f, "\\\\[6ex]"
        print >>f, "\\begin{tabular}{c c c}"
        print >>f, "~~~~~~~~~~~~~Name~~~~~~~~~~~~~ & ~~~~~~~~~Bid (\$)~~~~~~~~~  & ~~~Email Address (if not standard olin.edu)~~~\\"+"\\"
        for a in range(26): # print lines for bids
            print >>f, " & & \\"+"\\"
            print >>f, "\hline"
        print >>f, "\\end{tabular}"
        print >>f, "\\newpage"

        print >>g, "\subsection{"+handleLatexChars(title)+"}" # title
        print >>g, handleLatexChars(personName) # name
        print >>g, "\\\\"
        print >>g, "Starting Bid: "+handleLatexChars(addDollarSign(startingBid))
        print >>g, "\\newline"
        if (numWinners != '' and handleLatexChars(numWinners) != '1'):
            print >>g, "Number of winners: "+handleLatexChars(numWinners)
            print >>g, "\\newline"
        print >>g, handleLatexChars(description).rstrip() # description

print >>f, "\\end{document}"
print >>g, "\\end{document}"
