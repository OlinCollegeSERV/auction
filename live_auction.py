#! /usr/bin/python

import csv 

sample = open('FinalLiveAuction.csv', "rb")
readSample = csv.reader(sample)

f = open('live.tex','w')

print >>f, "\documentclass[11pt]{article}"
print >>f, "\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>f, "\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>f, "\setlength{\parindent}{0in}"
print >>f, "\\begin{document}"

for item in readSample:
	#print item[1]+"\n"
	print >>f, "\subsection{"+item[2]+"}" # title
	print >>f, item[0] # who's donating it
	print >>f, "\\newline"
	print >>f, "Starting Bid: \\"+item[3] # starting bid amount
	print >>f, "\\newline"
	print >>f, item[4] # description

print >>f, "\\end{document}"
