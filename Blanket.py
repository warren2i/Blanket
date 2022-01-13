import re
import string
import random
import io
findvar = re.compile(r'(?<=\$)(.*?)(?=[\s,),\.,=,\",\;])') ## lockback search for $ look forward search for end char or space
vararray = []
randomvararray=[]
f = open("scripts/shell.ps1", "rt")
lines = f.readlines()
f.close()
f = open("scripts/shell.ps1", "rt")

w = open("scripts/newshell.txt", "wt")
script = f.read()
f.close()
list =[
	"System.Net.Sockets.TcpClient",
    "System.IO.StreamWriter",
	"System.Byte",
	"System.Text.Encoding",
	"System.Text.AsciiEncoding",
	"System.Diagnostics.Process",
	"System.Text.ASCIIEncoding",
	"Net.Sockets.TCPClient",
	"System.Net.Networkinformation.Ping",
	"PSObject",
	"Net.WebClient",
	"System.Net.HttpListener",
	"Security.Principal.WindowsPrincipal",
	"System.Net.IPEndPoint",
	"TExT.AscIIENcoDINg",
	"io.strEamWritEr"
]
def whitespace():
    ##this function will add random amounts of whitespace at the start of each line
    pass

def stripcomments():
    ##this function will strip the input script of all comments. Perhaps better to replace the comment
    pass

def convertcase(): ## this function will alternate case ie WrItE-HoSt
    pass

def addcomments(): ## inserts a comment on each line
    transcript = open("transcripts/rickandmorty.txt", "rt")
    for num, aline in enumerate(transcript, 2):
        if random.randrange(num):
            continue
        line = aline
        line = re.sub('[\W]', ' ', line) ## anything that is not a word, replace with whitespace ' '
    return '<# '+ line + ' #>' ## returns the stripped line with inline comment tags

def randomvar(length): ##create a random variable of len length
    letters = string.ascii_letters
    randomvar=(''.join(random.choice(letters) for i in range(length)))  ##creates a random string of length randomlen
    return randomvar

def breakdatatype(string,rando):
    breakdataarr=[]
    n = random.randrange(3,7) # chunk length
    chunks = [string[i:i+n] for i in range(0, len(string), n)]
    for x in enumerate(chunks):
        breakdataarr.append(['$'+randomvar(rando),x[1]])
    newstring=("".join('%s'%item[0] for item in breakdataarr))

    return breakdataarr,newstring

for line in lines: ## itterate line by line
    lines = findvar.finditer(line) ##match variables
    for var in lines: ## loop over variables
        #print(var)
        var = var.group(0) ## pass index of the group, strips what we dont want.
        if var not in vararray: ## don't populate array with same value twice
            vararray.append('$'+var) ## add found var to vararray
            randomvararray.append('$'+randomvar(10)) ## add random var to randomvar array at matching index

    for x in enumerate(vararray): ## replace variables with random variables
        script = script.replace(vararray[x[0]], randomvararray[x[0]])
varr=[]
s = io.StringIO(script) ## used to itterate string 'line by line...'
for line in s:
    print(line)
    for l in list:
        if l in line:
            b = breakdatatype(l, random.randrange(3, 14))  ## pass string and random length to breakdata function
            # print(line)
            line = line.replace(l, b[1])
            # print(line)
            # print((b[1])+l) ##just to debug
            for a in enumerate(b[0]):
                varr.append((b[0][a[0]][0]) + ' = "' + b[0][a[0]][
                    1] + '"')  ##formats into powershell variable format ie $MUI = "Syst"
    script = script + line
s = io.StringIO(script) ## used to itterate string 'line by line...'

w.write("\n".join(varr))
w.write("\n")
for line in s:
    w.write(line) ## write line to file
    w.write(addcomments() + '\n') ## write comment line to file




