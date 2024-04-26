from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
from unidecode import unidecode
master = Tk()

font = ImageFont.truetype("bahnschrift.ttf",22)
def writeDefense(team):
    img = Image.open('templates/defensetemplate.png')
    draw = ImageDraw.Draw(img)
    for i in range(len(playerNameLabels)):
        surname = playerNames[i].get()
        surname = surname[surname.find(' '):].upper()
        position = playerPositions[i].get()
        change = shirtNumbers[i].get('1.0', 'end-1c')
        if change=='X':
            colors = (255,255,0)
        else:
            colors = (255,255,255)
        if (team=='away' and i%2==0) or (team == 'home' and i%2==1):
            if position=='C':
                draw.text((1673-font.getlength(surname)/2,527),surname,colors,font=font)
            elif position=='CF':
                draw.text((1673-font.getlength(surname)/2,263),surname,colors,font=font)
            elif position=='1B':
                draw.text((1836-font.getlength(surname)/2,432),surname,colors,font=font)
            elif position=='3B':
                draw.text((1511-font.getlength(surname)/2,432),surname,colors,font=font)
            elif position=='SS':
                draw.text((1583-font.getlength(surname)/2,375),surname,colors,font=font)
            elif position=='2B':
                draw.text((1764-font.getlength(surname)/2,375),surname,colors,font=font)
            elif position=='LF':
                draw.text((1511-font.getlength(surname)/2,299),surname,colors,font=font)       
            elif position=='RF':
                draw.text((1836-font.getlength(surname)/2,299),surname,colors,font=font)   
            elif position=='P':
                draw.text((1673-font.getlength(surname)/2,468),surname,colors,font=font)                 

    img.save('working_graphics/workingdefense.png')
    img.close()

    img = Image.open("templates/lineupsmallbase.png")
    draw = ImageDraw.Draw(img)
    lo=1
    nameString=""
    positionString=""
    tfont = ImageFont.truetype("bahnschrift.ttf",40)
    if team=='home':
        draw.text((1550,585),"AWAY LINEUP", (255,255,255),font=tfont)
    elif team=='away':
        draw.text((1550,585),"HOME LINEUP", (255,255,255),font=tfont)
    tfont = ImageFont.truetype("bahnschrift.ttf",24)
    for i in range(len(playerNameLabels)):
        name = playerNames[i].get()
        position = playerPositions[i].get()
        if (team=='home' and i%2==0) or (team == 'away' and i%2==1):
            if lo<10:
                nameString+=str(lo)+". "+name+"\n"
                lo+=1
                positionString+=position+"\n"
    draw.text((1518,660),nameString,(255,255,255),font=tfont)
    draw.text((1800,660),positionString,(255,255,255),font=tfont)
    img.save('working_graphics/workinglineup.png')
    img.close()

    img = Image.open("templates/bigdefensebase.png")
    draw=ImageDraw.Draw(img)
    tfont = ImageFont.truetype("bahnschrift.ttf",20)
    for i in range(len(playerNameLabels)):
        if (team=='away' and i%2==0) or (team == 'home' and i%2==1):
            name = playerNames[i].get()
            position = playerPositions[i].get()
            try:
                modifiedName = "#"+shirtNumbers[i].get('1.0', 'end-1c')+" "+name[0]+"."+name[name.find(' '):]
            except:
                modifiedName=""
            if i%2==0:
                teamname = awayteamname.get()
            else:
                teamname = hometeamname.get()
            try:
                portrait = Image.open('portraits/'+teamname+"/"+name+'.png')
                portrait = portrait.resize((280,200),Image.LANCZOS)
            except:
                portrait = 123415
            
            coords = (-1,-1)
            if position=="C":
                coords=(872,701)
            if position=="3B":
                coords=(162,563)
            if position=="SS":
                coords=(495,415)
            if position=="LF":
                coords=(251,62)
            if position=="CF":
                coords=(872,51)
            if position=="P":
                coords=(872,375)
            if position=="RF":
                coords=(1488,62)   
            if position=="2B":
                coords=(1250,415)
            if position=="1B":
                coords=(1583,563)
            if position!="DH":  
                draw.text((88+coords[0]-tfont.getlength(modifiedName)/2,coords[1]+260),modifiedName,(255,255,255),font=tfont) 
            try:
                adjc = (coords[0]-50,coords[1]+50)
                if position!="DH":
                    img.paste(portrait,adjc)
            except:
                continue            
                
    img.save("working_graphics/workingbigdefense.png")
    img.close()
#1788,460

tl = Label(master, text="Away team:")
tl.grid(row=0, column=1, sticky=W, pady=2)
htl = Label(master, text="Home team:")
htl.grid(row=0, column=5, sticky=W, pady=2)

teams = ["team", "Stal", "Silesia", "Gepardy", "Barons", "Centaury", "Rawa", "Dęby", "Piraci"]

awayteamname = StringVar(master)

hometeamname = StringVar(master)

tc = OptionMenu(master, awayteamname, *teams )
tc.grid(row=1, column=1, pady=2 )

htc = OptionMenu(master, hometeamname, *teams )
htc.grid(row=1, column=5, pady=2 )

positionList = ["POS","P", "C", "1B", '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH', 'PH', 'PR']


def filename(alt, team):
    if alt==2:
        return team+"_alt.png"
    return team+".png"

def fetchRosters(team, year):
    roster = []
    f = open('rosters/'+team+str(year)+'.txt', 'r', encoding='UTF-8')
    for x in f:
        roster.append(x.rstrip('\n'))
    f.close()
    return roster

def button_thing():
    away_game = filename(nonbreakcoloraway.get(),awayteamname.get())
    home_game = filename(nonbreakcolorhome.get(),hometeamname.get())
    away_break = filename(0,awayteamname.get())
    home_break = filename(0,hometeamname.get())

    base = Image.open("templates/base.png")
    ag = Image.open("away/"+away_game)
    hg = Image.open("home/"+home_game)
    bases = Image.open("templates/basebases.png")

    base.paste(ag, (0, 0), ag)
    base.paste(hg, (0, 0), hg)
    base.paste(bases, (0, 0), bases)

    base.save("working_graphics/workinggamebase.png")
    base.close()
    ag.close()
    hg.close()
    bases.close()

    breakaway = Image.open("secondaway/"+away_break)
    breakhome = Image.open("secondhome/"+home_break)
    breakaway.paste(breakhome,(0,0),breakhome)
    breakaway.save("working_graphics/workinggamebreak.png")
    breakaway.close()
    breakhome.close()

    for widget in playerNameLabels:
        widget.grid_forget()

    for i in range(len(playerNameLabels)):
        if i%2==0:
            playerNameLabels[i] = OptionMenu(master, 
                                            playerNames[i],
                                            *fetchRosters(awayteamname.get(),2024))
        else:
            playerNameLabels[i] = OptionMenu(master, 
                                            playerNames[i],
                                            *fetchRosters(hometeamname.get(),2024))
    for i in range(10):
        playerNameLabels[2*i].grid(row=4+i, column=1)
        playerNameLabels[2*i+1].grid(row=4+i, column=5)


    

confirmbutton = Button(master, text='confirm teams', command=button_thing)
confirmbutton.grid(row=1,column=8)


nonbreakcoloraway=IntVar(master)
primarycoloraway = Checkbutton(master, text="secondary?", variable=nonbreakcoloraway, offvalue=1, onvalue=2)
nonbreakcolorhome=IntVar(master)
primarycolorhome = Checkbutton(master, text="secondary?", variable=nonbreakcolorhome, offvalue=1, onvalue=2)


primarycoloraway.grid(row=2, column=1, pady=2 )
primarycolorhome.grid(row=2, column=5, pady=2 )


shirtNumbers = []
playerNames = []
playerNameLabels = []
playerPositionLabels = []
playerPositions = []
acceptButtons = []

def formatSlashString(stat, df):
    st = '%.3f' % df[stat].values[0]
    if st[0]=='0':
        return st[1:]
    else:
        return st

def statbutton(i):
    battingOrder = int(i/2)+1
    activeNumber = shirtNumbers[i].get('1.0', 'end-1c')
    activeName = playerNames[i].get()
    activePos = playerPositions[i].get()
    depolishifiedName = unidecode(activeName)


#ImageFont.truetype("bahnschrift.ttf",22)
    if battingOrder<10:
        file=open('working_graphics/workingBatter.txt', 'w', encoding='UTF-8')
        battingString = str(battingOrder)+". "+activeName
        
        file.write(battingString)
        file.close()
    else:
        file=open('working_graphics/workingPitcher.txt', 'w', encoding='UTF-8')
        battingString = "P. "+activeName
        
        file.write(battingString)
        file.close()

    background = Image.open('templates/playerNoStatBase.png')
    draw = ImageDraw.Draw(background)
    if activeNumber!="":
        playerNo = "#"+activeNumber+" "
    else:
        playerNo = ""
    nameString = playerNo+activeName.upper()


    draw.text((439,874), nameString, (255,255,255), font=ImageFont.truetype("bahnschrift.ttf",40))

    if i%2==0:
        team = awayteamname.get()
    else:
        team = hometeamname.get()

    try:
        portrait = Image.open('portraits/'+team+"/"+activeName+'.png')
        background.paste(portrait, (1142,613) )
        portrait.close()
    except:
        print("couldn't load picture for",activeName)
    background.save('working_graphics/workingstats.png')
    background.close()



for i in range(20):
    shirtNumbers.append(Text(master, height=1, width=2))
    playerNames.append(StringVar(master,""))
    playerPositions.append(StringVar(master,""))
    playerNameLabels.append(Text(master, height=1, width=20))
    playerPositionLabels.append(OptionMenu(master, playerPositions[i], *positionList ))
    acceptButtons.append(Button(master, text="STAT", width=4, command=lambda i=i:statbutton(i)))



for i in range(10):
    shirtNumbers[2*i].grid(row=4+i, column=0)
    playerNameLabels[2*i].grid(row=4+i, column=1) #playerNames
    playerPositionLabels[2*i].grid(row=4+i,column=2)
    acceptButtons[2*i].grid(row=4+i,column=3)
    shirtNumbers[2*i+1].grid(row=4+i, column=4)
    playerNameLabels[2*i+1].grid(row=4+i, column=5)
    playerPositionLabels[2*i+1].grid(row=4+i,column=6)
    acceptButtons[2*i+1].grid(row=4+i,column=7)

playerPositions[18].set("P")
playerPositions[19].set("P")

global balls, strikes, innings, middleFlag
balls=0
strikes=0
innings = 0
middleFlag = True
def addCount(what,increment):
    global balls
    global strikes
    if what=="balls":
        balls = balls+increment
    elif what=="strikes":
        strikes = strikes+increment

    f = open('working_graphics/count.txt', 'w')
    f.write(str(balls)+"-"+str(strikes))
    f.close()
def resetCount():
    global balls
    global strikes    
    balls = 0
    strikes = 0
    f = open('working_graphics/count.txt', 'w')
    f.write(str(balls)+"-"+str(strikes))
    f.close()
def addInnings(increment):
    global innings
    innings = innings+increment
    f = open('working_graphics/innings.txt', 'w')
    f.write(str(innings)+'. INNING')
    f.close()
def betweenInnings():
    global middleFlag
    f = open('working_graphics/betweenInnings.txt','w',encoding='UTF-8')
    if not middleFlag:
        middleFlag = True
        f.write('ŚRODEK '+str(innings)+'. ZMIANY')
    else:
        middleFlag = False
        f.write('PO '+str(innings)+'. ZMIANIE')
    f.close()
            
ballLabel = Label(master, text="balls")
ballPlusButton = Button(master, text="+", width=1,  command=lambda:addCount("balls",1))
ballMinusBotton = Button(master, text="-", width=1, command=lambda:addCount("balls",-1))
ballReset = Button(master, text="0", width=1, command=lambda:addCount("balls",-balls))

strikeLabel = Label(master, text="strike")
strikePlusButton = Button(master, text="+", width=1,  command=lambda:addCount("strikes",1))
strikeMinusBotton = Button(master, text="-", width=1, command=lambda:addCount("strikes",-1))
strikeReset = Button(master, text="0", width=1, command=lambda:addCount("strikes",-strikes))

resetButton = Button(master, text="Reset", width=5, command=resetCount)

inningsLabel = Label(master, text="innings")
inningsPlusButton = Button(master, text="+", width=1,  command=lambda:addInnings(1))
inningsMinusBotton = Button(master, text="-", width=1, command=lambda:addInnings(-1))

inningsMidButton = Button(master, text="mid", width=4,  command=lambda:betweenInnings())
inningsEndButton = Button(master, text="end", width=4,  command=lambda:betweenInnings())

getAwayDefense = Button(master, text="away def", width=8,  command=lambda:writeDefense('away'))
getHomeDefense = Button(master, text="home def", width=8,  command=lambda:writeDefense('home'))

ballLabel.grid(row=4, column=8)
ballPlusButton.grid(row=5, column=8)
ballMinusBotton.grid(row=6, column=8)
ballReset.grid(row=7, column=8)
strikeLabel.grid(row=8, column=8)
strikePlusButton.grid(row=9, column=8)
strikeMinusBotton.grid(row=10, column=8)
strikeReset.grid(row=11, column=8)
resetButton.grid(row=12, column=8)
inningsLabel.grid(row=4, column=9)
inningsPlusButton.grid(row=5, column=9)
inningsMinusBotton.grid(row=6, column=9)
inningsMidButton.grid(row=7, column=9)
inningsEndButton.grid(row=8, column=9)
getAwayDefense.grid(row=9, column=9)
getHomeDefense.grid(row=10, column=9)
master.mainloop()