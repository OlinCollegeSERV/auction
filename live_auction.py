#! /usr/bin/python

import csv 

def addDollarSign(amt):
    if amt[0] == '$':
        return amt
    else:
        return '$'+amt

def handleLatexChars(s):
    return s.replace("$","\\$").replace("&","\\&").replace("#","\\#").replace("^","\\^")

sample = open('2014/FinalLiveAuction.csv', "rb")
readSample = csv.reader(sample,delimiter='|',quotechar='%')

f = open('2014/live.tex','w')

print >>f, "\documentclass[11pt]{article}"
print >>f, "\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>f, "\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>f, "\setlength{\parindent}{0in}"
print >>f, "\\title{Live Auction Donation Packet}"
print >>f, "\\author{SERV Auction 2014}"
print >>f, "\\date{November 14th, 2014}"
print >>f, "\\begin{document}"
print >>f, "\\maketitle"

for item in readSample:
    print >>f, "\subsection{"+handleLatexChars(item[2])+"}" # title
    print >>f, handleLatexChars(item[0]) # name
    print >>f, "\\\\"
    print >>f, "Starting Bid: "+handleLatexChars(addDollarSign(item[3]))
    print >>f, "\\newline"
    print >>f, handleLatexChars(item[4]).rstrip() # description

print >>f, "\\end{document}"
