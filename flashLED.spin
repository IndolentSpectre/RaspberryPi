' Program to flash a LED by each cog
' Cog 0 is the main controller
'
' Indicate to PI by manipulating I/O pins
'
' Chris Noble
' 03-Jan-2019

VAR
byte cogNUM
byte thisCog
long cogMEM[120]
byte semID
byte numCog[8]

CON
indCog0 = 22
indCog1 = 23
indCog2 = 24
indCog3 = 25
indCog4 = 26
indCog5 = 27
indCog6 = 28
indCog7 = 29

PUB main
	numCog[0] := indCog0
	numCog[1] := indCog1
	numCog[2] := indCog2
	numCog[3] := indCog3
	numCog[4] := indCog4
	numCog[5] := indCog5
	numCog[6] := indCog6
	numCog[7] := indCog7

	DIRA := %00111111_11000000_00000000_00000011
	' switch all on then on
	outa[29..22]~
	waitcnt(cnt + clkfreq) ' wait 1 second
	outa[29..22]~~

	thisCog := numCog[COGID]
	outa[thisCog] := 1 ' indicate running status

	' Indicate program initialisations
	outa[0] := 1 ' light LED 0
	outa[1] := 1 ' light LED 1
	waitcnt(cnt + clkfreq*5) ' wait 5 seconds
	outa[0] := 0 ' light LED 0
	outa[1] := 0 ' light LED 1
	' get a semaphore lock
	if (SemID := locknew) == -1 ' no lock available!
		!outa[0]
		waitcnt(cnt + clkfreq/2)
		!outa[0]
		waitcnt(cnt + clkfreq/2)
		!outa[0]
		waitcnt(cnt + clkfreq/2)
		'outa[1] := 0
    		cogstop(0)
  	else
		repeat ' endless loop
			repeat  cogNUM from 1 to 7 ' round robin cogs
				waitcnt(cnt + clkfreq)
				outa[0] := 1
				outa[1] := 1
				waitcnt(cnt + clkfreq)
				outa[0] := 0
				outa[1] := 0
				longfill(@cogMEM, 0, 120) ' clear cog memory
				outa[numCog[cogNUM]] := 1
				coginit(cogNUM, flash_LED, @cogMEM)
				repeat until not lockset(semID) ' wait until cog clears the lock
				outa[numCog[cogNUM]] := 0
                		'waitcnt(cnt + clkfreq) ' wait 1 second before stopping cog
				cogstop(cogNUM)

PRI flash_LED
thisCog := numCog[COGID]
DIRA[1..0]~~

outa[1] := 1
waitcnt(cnt + clkfreq * 2) ' wait 2 seconds
repeat COGID
	outa[0] := 1
	waitcnt(cnt + clkfreq)
	outa[0] := 0
	waitcnt(cnt + clkfreq)

lockclr(semID) ' clear the lock
