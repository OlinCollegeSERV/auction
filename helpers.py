def addDollarSign(amt):
    if amt[0] == '$':
        return amt
    else:
        return '$'+amt

def handleLatexChars(s):
    return (
        s.replace("$","\\$")
        .replace("&","\\&")
        .replace("#","\\#")
        .replace("^","\\^")
        .replace("_","\\_")
        .replace("\^\^","^^")
        .replace("%","\\%")
        .replace(">", "\\textgreater ")
        .replace("<", "\\textless ")
    )
