import sys

def uniqthis(fileName): #sort/uniq input
    my_list = sorted(set(fileName))
    return my_list

def stripIt(unmodified):
    removeHTTP = unmodified.split("/")[3:]  #strip from 3rd '/' onward with /'s eg. http://abc.com/ <-
    return removeHTTP

def findSubDirs():
    inFile = sys.argv[1]    #get our unedited list of ursl
    with open(inFile, 'r') as i:    #create a new list of all these urls
        lines = i.readlines()
    
    for i in range(len(lines)):
        lines[i] stripIt(lines[i]) #strip out directories
    separatedListUnsorted = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):  #pull out strings from total list
            text = lines[i][j].strip()
            separatedListUnsorted.append(text)
    
    separatedList = uniqthis(separatedListUnsorted)
    outFile = sys.argv[2]

    with open(outFile, 'w') as out:
        for line in separatedList:
            if '&' in line or '?' in line or ':' in line or '.' in line:    #only want directories, not filenames or params
                pass
            else:
                out.write(line + "\n")

def startup():
    if len(sys.argv) == 1:
        print("must provide input file")
    elif len(sys.argv) == 2:
        print("must provide output filename")
    elif len(sys.argv) == 3:
        findSubDirs():
    else:
        sys.exit()

startup()