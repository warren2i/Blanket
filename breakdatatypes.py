import re
import string
import random
import io

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
f = open("scripts/shell.ps1", "rt")
lines = f.readlines()
f.close()
f = open("scripts/shell.ps1", "rt")

w = open("scripts/newshell1.txt", "wt")

f.close()

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

varr=[]
script=""
for line in lines:
	#print(line)
	for l in list:
		if l in line:
			b = breakdatatype(l,random.randrange(3,14)) ## pass string and random length to breakdata function
			#print(line)
			line=line.replace(l,b[1])
			#print(line)
			#print((b[1])+l) ##just to debug
			for a in enumerate(b[0]):
				varr.append((b[0][a[0]][0])+' = "'+b[0][a[0]][1]+'"') ##formats into powershell variable format ie $MUI = "Syst"
	script=script+line
w.write("\n".join(varr))
w.write("\n")
w.write(script)
	#w.write(line)
	#print(line)
		#print(b)
#print(*lines)


#w.write("\n".join(varr))
#w.write("\n")


