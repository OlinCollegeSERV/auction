import csv
 
sample = open('FinalLiveAuction.csv', "rb")
readSample = csv.reader(sample)
 
f = open('servsheets.tex','w')
 
print >>f, "\documentclass[11pt]{article}"
print >>f, "\pagestyle{plain} \\topmargin -.5in \oddsidemargin 0in"
print >>f, "\evensidemargin 0in \\textwidth 6.5in \\textheight 8in"
print >>f, "\setlength{\parindent}{0in}"
print >>f, "\\begin{document}"

categories = [[],[],[],[],[]]
 
for item in readSample:
    if (item[5] == ""):
        categories[0].append(item)
    elif (item[5] == ""):
        categories[1].append(item)
    elif (item[5] == ""):
        categories[2].append(item)
    elif (item[5] == ""):
        categories[3].append(item)
    elif (item[5] == ""):
        categories[4].append(item)

for category in categories:
    for item in category:
        #print item[1]+"\n"
        print >>f, "\section{"+item[2]+"}"
        print >>f, item[0]
        print >>f, "\\newline"
        print >>f, "Starting Bid: \\"+item[3]
        print >>f, "\\newline"
        print >>f, item[4]
        print >>f, "\\newline"
        print >>f, "\\newline"
        print >>f, "\\begin{tabular}{c c c}"
        print >>f, "~~~~~~~~~~~~~Name~~~~~~~~~~~~~ & ~~~~~~~~~Bid~~~~~~~~~  & ~~~~~~~~~~~~~Email Address (if different name or not standard olin.edu)~~~~~~~~~~~~~\\"+"\\"
        for a in range(19):
            print >>f, " & & & \\"+"\\"
            print >>f, "\hline"
        print >>f, "\\end{tabular}"
        print >>f, "\\newpage"

print >>f, "\\end{document}"