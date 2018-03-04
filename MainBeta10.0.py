import pygame
import random
from Settings import *
vec = pygame.math.Vector2

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
ball = pygame.image.load("Balls/ball_1.png")  #the ball file has be croped
ballRot = pygame.image.load("Balls/ball_1 copy.png")  #the ball file has be croped
StartButton = pygame.image.load("Graphics/btn_play.png")  #the ball file has be croped
ColorOfFields = GREEN
pygame.mouse.set_visible(0)
BurnSound = pygame.mixer.Sound("Sounds/earcing.ogg")

Info=pygame.image.load("Graphics/InfoPic.png")

Tutorial=pygame.image.load("Graphics/Tutorial.png")
TutorialBlack=pygame.image.load("Graphics/TutorialBlack.png")

GrassTile=pygame.image.load("Graphics/GrassTilePic.png")
GrassTileRoundedLeft=pygame.image.load("Graphics/GrassTileRoundedLeftPic.png")
GrassTileRoundedRight=pygame.image.load("Graphics/GrassTileRoundedRightPic.png")
GrassTileRoundedBoth=pygame.image.load("Graphics/GrassTileRoundedBothPic.png")


IceTile=pygame.image.load("Graphics/IceTilePic.png")
IceTileRoundedLeft=pygame.image.load("Graphics/IceTileRoundedLeftPic.png")
IceTileRoundedRight=pygame.image.load("Graphics/IceTileRoundedRightPic.png")
IceTileRoundedBoth=pygame.image.load("Graphics/IceTileRoundedBothPic.png")

CursorImage = pygame.image.load("Graphics/Cursor.png")
CursorImage = pygame.transform.scale(CursorImage,(50,50))

backG = pygame.image.load("Backgrounds/ga_bg_8.jpg")

MenuBackG = pygame.image.load("Backgrounds/ga_bg_7.jpg")
MenuBackG = pygame.transform.scale(MenuBackG, BackGroundSize)

SettingButton = pygame.image.load("Graphics/SettingsButtonPic.png")
#SettingButton = pygame.transform.scale(SettingButton, (80,80))

InfoButton = pygame.image.load("Graphics/InfoButtonPic.png")
#InfoButton = pygame.transform.scale(InfoButton, (90,90))

BackButton = pygame.image.load("Graphics/BackButtonPic.png")
BackButton = pygame.transform.scale(BackButton, (90,90))
BackButtonLight = pygame.image.load("Graphics/BackButtonPicLight.png")
BackButtonLight = pygame.transform.scale(BackButtonLight, (90,90))

ForwardButton = pygame.image.load("Graphics/ForwardButtonPic.png")
ForwardButton = pygame.transform.scale(ForwardButton, (90,90))
ForwardButtonLight = pygame.image.load("Graphics/ForwardButtonPicLight.png")
ForwardButtonLight = pygame.transform.scale(ForwardButtonLight, (90,90))

GrassPic = pygame.image.load("Graphics/GRASSPngFile.png")
GrassPic = pygame.transform.scale(GrassPic, (400,100))

IcePic = pygame.image.load("Graphics/icePicture.png")
IcePic = pygame.transform.scale(IcePic, (400,100))

CustomizePic = pygame.image.load("Graphics/btn_shop.png")
#CustomizePic = pygame.transform.scale(CustomizePic, (100,100))

Lock = pygame.image.load("Graphics/LockPic.png")
Lock = pygame.transform.scale(Lock, (150,150))

UnLock = pygame.image.load("Graphics/UnLockPic.png")
UnLock = pygame.transform.scale(UnLock, (200,200))

PauseButton = pygame.image.load("Graphics/PauseButtonPic.png")
PauseButton = pygame.transform.scale(PauseButton, (100,100))

ConfirmationWindow = pygame.image.load("Graphics/ConfirmationPic.png")
NoMoneyWindow = pygame.image.load("Graphics/NoMoneyWindowPic.png")
PauseWindow = pygame.image.load("Graphics/PauseWindowPic.png")
GameOverWindow = pygame.image.load("Graphics/GameOverWindowPic.png")

#ConfirmationWindow = pygame.transform.scale(ConfirmationWindow, (500,200))

ListOfBallsNumbers=[None]*29
ListOfBallsRotNumbers=[None]*29
TempStr = ""
for index in range (0,29):
    TempStr="Balls/"
    TempStr+="ball_"
    TempStr+=str(index+1)
    TempStr+=".png"
    ListOfBallsNumbers[index]=TempStr
    TempStr="Balls/"
    TempStr+="ball_"
    TempStr+=str(index+1)
    TempStr+=" copy"
    TempStr+=".png"
    ListOfBallsRotNumbers[index]=TempStr
BallUsing = 0

ListOfBackGrounds=[None]*16
ListOfMiniBackGrounds=[None]*16
TempStr = ""
for index in range (0,16):
    TempStr="Backgrounds/"
    TempStr+="ga_bg_"
    TempStr+=str(index+1)
    TempStr+=".jpg"
    ListOfBackGrounds[index]=TempStr
    TempStr="Backgrounds/"
    TempStr+="cus_bg_"
    TempStr+=str(index+1)
    TempStr+=".png"
    ListOfMiniBackGrounds[index]=TempStr
BackGroundUsing = 0

Player_Score = 0

Player_High_Score=0

Player_Money=0

HighScoreReachingVar=0


ListPurchasedBalls=[]
ListPurchasedBackGrounds=[]
ListBallPrice=[]
ListBackGroundPrice=[]

BallPos = vec(150,300)
BallVel = vec(0,0)
BallAcc = vec(0,0)

rotate = False
Laser={"xPos":0 , "yPos":10 , "L_Width":WIDTH , "L_Color":RED , "speed": Laser_Speed}

field0={"space":[0,0,0,0,0,0,1] , "yPos":570 , "F_Color":ColorOfFields}
field1={"space":[0,0,0,0,0,0,1] , "yPos":430 , "F_Color":ColorOfFields}
field2={"space":[0,0,0,0,0,0,1] , "yPos":290 , "F_Color":ColorOfFields}
field3={"space":[0,0,0,0,0,0,1] , "yPos":150 , "F_Color":ColorOfFields}
field4={"space":[0,0,0,0,0,0,1] , "yPos":10 , "F_Color":ColorOfFields}

field = [field0,field1,field2,field3,field4]
fieldVel=5

PowerUpKinds={"SpeedUp":"Graphics/ga_item_Speed.png","FieldRemove":"Graphics/ga_item_Fall.png","Scorex2":"Graphics/ga_item_Money_Maker.png","LaserStop":"Graphics/ga_item_Laser_Stop.png"}

PowerUp={"Kind":PowerUpKinds["SpeedUp"] , "xPos":20 , "yPos":305 , "vel":0}

fonts={"San":'Fonts/sanFranciscoFont.ttf',"Auth":'Fonts/UnderAuthority.ttf'}

Grass=True
Ice = False

ScoreColor = WHITE

def SourceFileReading():
    global Player_High_Score
    global Player_Money
    global ListPurchasedBalls
    global ListPurchasedBackGrounds
    global ListBallPrice
    global ListBackGroundPrice
    global BallUsing
    global BackGroundUsing
    FileRead = open("SourceCSV.txt","r+")
    SourceFileList=FileRead.read().split("\n")
    ListScoreMoney = SourceFileList[0].split(",")
    ListPurchasedBalls = SourceFileList[1].split(",")
    ListPurchasedBackGrounds = SourceFileList[2].split(",")
    ListBallPrice = SourceFileList[3].split(",")
    ListBackGroundPrice = SourceFileList[4].split(",")
    ListUsings=SourceFileList[5].split(",")
    Player_High_Score=int(ListScoreMoney[0])
    Player_Money=int(ListScoreMoney[1])
    BallUsing=int(ListUsings[0])
    BackGroundUsing=int(ListUsings[1])
    FileRead.close()
def SourceFileWriting():
    FileWrite = open("SourceCSV.txt","w")
    FileWrite.write(str(Player_High_Score))
    FileWrite.write(",")
    FileWrite.write(str(Player_Money))
    FileWrite.write("\n")
    for index in range (0,len(ListPurchasedBalls)):    #RECORDING THE PURCHASED BALLS
        FileWrite.write(ListPurchasedBalls[index])
        if len(ListPurchasedBalls)-1 != index:
            FileWrite.write(',')
    FileWrite.write("\n")
    for index in range (0,len(ListPurchasedBackGrounds)):    #RECORDING THE PURCHASED Backgrounds
        FileWrite.write(ListPurchasedBackGrounds[index])
        if len(ListPurchasedBackGrounds)-1 != index:
            FileWrite.write(',')
    FileWrite.write("\n")
    for index in range (0,len(ListBallPrice)):    #RECORDING THE BALL PRICE
        FileWrite.write(ListBallPrice[index])
        if len(ListBallPrice)-1 != index:
            FileWrite.write(',')
    FileWrite.write("\n")
    for index in range (0,len(ListBackGroundPrice)):    #RECORDING THE BACKGROUND PRICE
        FileWrite.write(ListBackGroundPrice[index])
        if len(ListBackGroundPrice)-1 != index:
            FileWrite.write(',')
    FileWrite.write("\n")
    FileWrite.write(str(BallUsing))
    FileWrite.write(",")
    FileWrite.write(str(BackGroundUsing))
    FileWrite.write("\n")
SourceFileReading()
touching = -1
#Game Main Loop
def resetGame():
    global field0
    global field1
    global field2
    global field3
    global field4
    global field
    global fieldVel
    global Laser_Speed
    global Laser
    global BallPos
    global BallVel
    global BallAcc
    global Player_Score
    global HighScoreReachingVar

    Player_Score=0

    BallPos = vec(150,300)
    BallVel = vec(0,0)
    BallAcc = vec(0,0)
    Laser_Speed=3
    Laser={"xPos":0 , "yPos":10 , "L_Width":WIDTH , "L_Color":RED , "speed": Laser_Speed}

    field0={"space":[0,0,0,0,0,0,1] , "yPos":570 , "F_Color":ColorOfFields}
    field1={"space":[0,0,0,0,0,0,1] , "yPos":430 , "F_Color":ColorOfFields}
    field2={"space":[0,0,0,0,0,0,1] , "yPos":290 , "F_Color":ColorOfFields}
    field3={"space":[0,0,0,0,0,0,1] , "yPos":150 , "F_Color":ColorOfFields}
    field4={"space":[0,0,0,0,0,0,1] , "yPos":10 , "F_Color":ColorOfFields}

    field = [field0,field1,field2,field3,field4]
    fieldVel=10

    HighScoreReachingVar=0
def GameOver():
    GameOverRunning = True
    while GameOverRunning:
        for event in pygame.event.get():
            clock.tick(30)
            if event.type == pygame.QUIT:
                GameOverRunning = False
                SourceFileWriting()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>=100 and x<=290 and y>=510 and y<=625:# Retry
                    return True
                elif x>=325 and x<=715 and y>=510 and y<=625:# MainMenu
                    return False

        screen.fill(BLACK)
        screen.blit(backG,(0,0))
        screen.blit(GameOverWindow,(50,50))
        if Player_Score/100 > 1:
            texts(str(Player_Score),250,280,70,(210,210,210),"San")
        elif Player_Score/10 > 1:
            texts(str(Player_Score),262,280,70,(210,210,210),"San")
        elif Player_Score/1 > 1:
            texts(str(Player_Score),285,280,70,(210,210,210),"San")
        if Player_High_Score/100 > 1:
            texts(str(Player_High_Score),250,415,70,(210,210,210),"San")
        elif Player_High_Score/10 > 1:
            texts(str(Player_High_Score),262,415,70,(210,210,210),"San")
        elif Player_High_Score/1 > 1:
            texts(str(Player_High_Score),285,415,70,(210,210,210),"San")
        x,y = pygame.mouse.get_pos()
        screen.blit(CursorImage,(x,y))
        pygame.display.flip()
def LoadBackG(BackGNumber):
    global backG
    backG = pygame.image.load(ListOfBackGrounds[BackGNumber])
def LoadBalls(BallNumber):
    global ball
    global ballRot
    ball = pygame.image.load(ListOfBallsNumbers[BallNumber])  #the ball file has be croped
    ballRot = pygame.image.load(ListOfBallsRotNumbers[BallNumber])
def drawBall(x,y,rotating):
    if rotating:
        screen.blit(ballRot,(x,y))
    else:
        screen.blit(ball,(x,y))
def drawPowerUp(x,y):
    screen.blit(pygame.image.load(PowerUp["Kind"]),(x,y))
def DrawField(FieldNumber,fieldY, fieldColor):
    if Grass == True:
        for index in range (0,6):
            if field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==1 and field[FieldNumber]["space"][index+1]==1:
                screen.blit(GrassTile,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==1 and field[FieldNumber]["space"][index+1]==0:
                screen.blit(GrassTileRoundedRight,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==0 and field[FieldNumber]["space"][index+1]==1:
                screen.blit(GrassTileRoundedLeft,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==0 and field[FieldNumber]["space"][index+1]==0:
                screen.blit(GrassTileRoundedBoth,(index*100,fieldY))

                #pygame.draw.rect(screen, fieldColor , [,fieldY,100,20])
    elif Ice == True:
        for index in range (0,6):
            if field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==1 and field[FieldNumber]["space"][index+1]==1:
                screen.blit(IceTile,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==1 and field[FieldNumber]["space"][index+1]==0:
                screen.blit(IceTileRoundedRight,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==0 and field[FieldNumber]["space"][index+1]==1:
                screen.blit(IceTileRoundedLeft,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==0 and field[FieldNumber]["space"][index+1]==1:
                screen.blit(IceTileRoundedLeft,(index*100,fieldY))
            elif field[FieldNumber]["space"][index]==1 and field[FieldNumber]["space"][index-1]==0 and field[FieldNumber]["space"][index+1]==0:
                screen.blit(IceTileRoundedBoth,(index*100,fieldY))

                #pygame.draw.rect(screen, fieldColor , [,fieldY,100,20])
def DrawLaser(LaserX,LaserY,LaserW, LaserColor):
    pygame.draw.rect(screen, LaserColor , [LaserX,LaserY,LaserW,5])
def RanTile(FieldNumber):
    Ra=random.randrange(1,3)
    for index in range (0,Ra):
        field[FieldNumber]["space"][random.randrange(0,6)]=0
def fieldReset(FieldNumber):
    field[FieldNumber]["yPos"]=HEIGHT+20
    for index in range (0,6):
        field[FieldNumber]["space"][index]=1
    RanTile(FieldNumber)
def PowerUpReset():
    global PowerUp
    Ra=random.randrange(0,5)
    PowerUp["yPos"]=520
    PowerUp["xPos"]=-30
    if Ra==0:
        PowerUp["Kind"]=PowerUpKinds["SpeedUp"]
    if Ra==1:
        PowerUp["Kind"]=PowerUpKinds["FieldRemove"]
    if Ra==2:
        PowerUp["Kind"]=PowerUpKinds["Scorex2"]
    if Ra==3:
        PowerUp["Kind"]=PowerUpKinds["LaserStop"]
def checkAbove():  #it has 2 purpose of updating the score and resetting a tile that went up
    for index in range (0,5):
        if field[index]["yPos"]< 0 :
            fieldReset(index)
            return True
def checkAbovePower():
    if PowerUp["yPos"]<-10 or PowerUp["yPos"]>HEIGHT+400:
        PowerUp["yPos"]=-100
        return True
    return False
def CheckTouch():
    for index in range (0,5):
        if field[index]["yPos"]==BallPos.y + 70 and field[index]["space"][int((BallPos.x+50)/100)]==1 :
            return True
            break
    return False
def CheckTouchPower():
    for index in range (0,5):
        if field[index]["yPos"]==PowerUp["yPos"] + 70 and field[index]["space"][int((PowerUp["xPos"]+50)/100)]==1:
            return True
            break
    return False
def GoUp():
    if CheckTouchPower() and PowerUp["yPos"]!=-20:
        PowerUp["yPos"]-=fieldVel
    for index in range (0,5):
        field[index]["yPos"] -= fieldVel
def DrawScore(score):
    font=pygame.font.Font('Fonts/sanFranciscoFont.ttf',30)
    scoretext=font.render("Score: "+str(score), 1,ScoreColor)
    screen.blit(scoretext, (10, 30))
def texts(words,x,y,size,TextColor,style):
    font=pygame.font.Font(fonts[style],size)
    Wordtext=font.render(words, 1,TextColor)
    screen.blit(Wordtext, (x, y))
def InfoPage():
    InfoRunning = True
    while InfoRunning:
        for event in pygame.event.get():
            clock.tick(30)
            if event.type == pygame.QUIT:
                InfoRunning = False
                SourceFileWriting()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>=10 and x<=90 and y>=10 and y<=90:
                    InfoRunning=False

        screen.fill(BLACK)
        screen.blit(MenuBackG,(0,0))
        screen.blit(BackButton,(10,10))
        screen.blit(Info,(70,70))
        x,y = pygame.mouse.get_pos()
        screen.blit(CursorImage,(x,y))
        pygame.display.flip()
def ShoppingPage():
    ShoppingRunning = True
    BallBuyingRequest=False
    BackGroundBuyingRequest=False
    global BallUsing
    global BackGroundUsing
    global Player_Money
    OnBall = BallUsing
    OnBackGround = BackGroundUsing
    while ShoppingRunning:
        for event in pygame.event.get():
            clock.tick(30)
            if event.type == pygame.QUIT:
                ShoppingRunning = False
                SourceFileWriting()
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>=10 and x<=90 and y>=10 and y<=90:  #back to the menu
                    ShoppingRunning=False
                elif (x>=100 and x<=190 and y>=210 and y<=300 and OnBall!=0 and BallBuyingRequest==False and BackGroundBuyingRequest==False):     #BALL CHANGE LEFT ARROW
                    if int(ListPurchasedBalls[OnBall-1])==1:
                        OnBall-=1
                        BallUsing = OnBall
                    else:
                        OnBall-=1
                elif (x>=420 and x<=510 and y>=210 and y<=300 and OnBall!=28 and BallBuyingRequest==False and BackGroundBuyingRequest==False):     #BALL CHANGE RIGHT ARROW
                    #print("onBall: ",OnBall)
                    #print("ball using: ",BallUsing)
                    if int(ListPurchasedBalls[OnBall+1])==1:
                        OnBall+=1
                        BallUsing = OnBall
                    else:
                        OnBall+=1
                elif (x>=100 and x<=190 and y>=490 and y<=580 and OnBackGround!=0 and BallBuyingRequest==False and BackGroundBuyingRequest==False):     # BACK GROUND CHANGE LEFT ARROW
                    if int(ListPurchasedBackGrounds[OnBackGround-1])==1:
                        OnBackGround-=1
                        BackGroundUsing = OnBackGround
                    else:
                        OnBackGround-=1
                elif (x>=420 and x<=510 and y>=490 and y<=580 and OnBackGround!=15 and BallBuyingRequest==False and BackGroundBuyingRequest==False):       #BACK GROUND CHANGE RIGHT ARROW
                    if int(ListPurchasedBackGrounds[OnBackGround+1])==1:
                        OnBackGround+=1
                        BackGroundUsing = OnBackGround
                    else:
                        OnBackGround+=1
                elif (x>=255 and x<=405 and y>=160 and y<=310 and BallBuyingRequest==False and BackGroundBuyingRequest==False and int(ListPurchasedBalls[OnBall])==0):       #Buying request balls
                    BallBuyingRequest=True
                elif (x>=230 and x<=380 and y>=440 and y<=590 and BallBuyingRequest==False and BackGroundBuyingRequest==False and int(ListPurchasedBackGrounds[OnBackGround])==0):       #Buying request balls
                    BackGroundBuyingRequest=True

                if BallBuyingRequest and Player_Money<int(ListBallPrice[OnBall]) and x>=240 and x<=340 and y>=361 and y<=411:#No Money
                    BallBuyingRequest=False

                if BallBuyingRequest and Player_Money>=int(ListBallPrice[OnBall]) and x>=110 and x<=195 and y>=371 and y<=426:#yes
                    Player_Money-=int(ListBallPrice[OnBall])
                    ListPurchasedBalls[OnBall]='1'
                    BallUsing=OnBall
                    BallBuyingRequest=False
                elif BallBuyingRequest and Player_Money>=int(ListBallPrice[OnBall]) and x>=405 and x<=505 and y>=371 and y<=426:#No
                    BallBuyingRequest=False
                ################################################
                if BackGroundBuyingRequest and Player_Money<int(ListBackGroundPrice[OnBackGround]) and x>=240 and x<=340 and y>=361 and y<=411:#No Money
                    BackGroundBuyingRequest=False

                if BackGroundBuyingRequest and Player_Money>=int(ListBackGroundPrice[OnBackGround]) and x>=110 and x<=195 and y>=371 and y<=426:#yes
                    Player_Money-=int(ListBackGroundPrice[OnBackGround])
                    ListPurchasedBackGrounds[OnBackGround]='1'
                    BackGroundUsing=OnBackGround
                    BackGroundBuyingRequest=False
                elif BackGroundBuyingRequest and Player_Money>=int(ListBackGroundPrice[OnBackGround]) and x>=405 and x<=505 and y>=371 and y<=426:#No
                    BackGroundBuyingRequest=False
        screen.fill(BLACK)
        screen.blit(MenuBackG,(0,0))
        screen.blit(BackButton,(10,10)) #top back button
        texts("Shop" , 240,50,60,(210,210,210),"Auth")

        texts("Buy New Balls From Here!:" , 135,140,30,(210,210,210),"Auth")                         #
        screen.blit(pygame.image.load(ListOfBallsNumbers[OnBall]),(250,210)) #       BALL SECTION
        if OnBall==0:
            screen.blit(BackButtonLight,(100,210))
        else:
            screen.blit(BackButton,(100,210))                                       #
        if OnBall==28:
            screen.blit(ForwardButtonLight,(420,210))
        else:
            screen.blit(ForwardButton,(420,210))                                    #

        texts("Buy New BackGrounds From Here!:" , 70,350,30,(210,210,210),"Auth")                            #
        screen.blit(pygame.image.load(ListOfMiniBackGrounds[OnBackGround]),(185,410))#   BACK GROUND SECTION
        if OnBackGround==0:
            screen.blit(BackButtonLight,(100,490))
        else:
            screen.blit(BackButton,(100,490))                                               #
        if OnBackGround==15:
            screen.blit(ForwardButtonLight,(420,490))
        else:
            screen.blit(ForwardButton,(420,490))
        if int(ListPurchasedBalls[OnBall])==1:
            screen.blit(UnLock,(170,140))
        elif int(ListPurchasedBalls[OnBall])==0:
            screen.blit(Lock,(225,160))
        if int(ListPurchasedBackGrounds[OnBackGround])==1:
            screen.blit(UnLock,(175,420))
        elif int(ListPurchasedBackGrounds[OnBackGround])==0:
            screen.blit(Lock,(230,440))
        if int(ListPurchasedBalls[OnBall])==0:
            texts("Price: "+str(ListBallPrice[OnBall]),250,300,25,BLUE,"San")
        if int(ListPurchasedBackGrounds[OnBackGround])==0:
            texts("Price: "+str(ListBackGroundPrice[OnBackGround]),250,510,25,BLUE,"San")
        texts("Money: "+str(Player_Money),240,10,25,(210,210,210),"San")

        if BallBuyingRequest and Player_Money<int(ListBallPrice[OnBall]):
            screen.blit(NoMoneyWindow,(50,231))
        elif BallBuyingRequest and Player_Money>=int(ListBallPrice[OnBall]):
            screen.blit(ConfirmationWindow,(50,231))
        ###########################
        if BackGroundBuyingRequest and Player_Money<int(ListBackGroundPrice[OnBackGround]):
            screen.blit(NoMoneyWindow,(50,231))
        elif BackGroundBuyingRequest and Player_Money>=int(ListBackGroundPrice[OnBackGround]):
            screen.blit(ConfirmationWindow,(50,231))

        x,y = pygame.mouse.get_pos()
        screen.blit(CursorImage,(x,y))
        pygame.display.flip()
def SettingsPage():
    SettingsRunning = True
    global Ice
    global Grass
    global ColorOfFields
    while SettingsRunning:
        for event in pygame.event.get():
            clock.tick(30)
            if event.type == pygame.QUIT:
                SettingsRunning = False
                SourceFileWriting()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>=10 and x<=90 and y>=10 and y<=90:
                    SettingsRunning=False
                elif (x>=20 and x<=110 and y>=280 and y<=370) or (x>=500 and x<=590 and y>=280 and y<=370):
                    if Grass:
                        Grass=False
                        Ice=True
                        Player_Accel=0.7
                        Player_Fric=-0.02
                        ColorOfFields = BLUE
                    elif Ice:
                        Grass=True
                        Ice=False
                        Player_Accel=0.55
                        Player_Fric=-0.05
                        ColorOfFields = GREEN
        screen.fill(BLACK)
        screen.blit(MenuBackG,(0,0))
        screen.blit(BackButton,(10,10))
        texts("Customize Playing Area With Arrows:" , 80,200,30,(210,210,210),"Auth")
        if Grass:
            screen.blit(GrassPic,(100,280))
        elif Ice:
            screen.blit(IcePic,(100,280))
        screen.blit(BackButton,(20,280))
        screen.blit(ForwardButton,(500,280))
        texts("Money: "+str(Player_Money),240,10,25,(210,210,210),"San")
        texts("High Score: "+str(Player_High_Score),220,60,25,(210,210,210),"San")
        x,y = pygame.mouse.get_pos()
        screen.blit(CursorImage,(x,y))
        pygame.display.flip()
def RunGame():
    PowerUpControl = 0
    running = True
    var = 0
    MouseMotion = False
    BallOnPower = False
    PowerUpTime=0
    global Player_Money
    global BallAcc
    global BallPos
    global BallVel
    global Player_Score
    global Player_High_Score
    global HighScoreReachingVar
    global Laser
    global fieldVel
    global Player_Fric
    global Laser_Speed
    global Grass
    global Ice
    global rotate
    global Player_Accel
    global RED
    while running:
        clock.tick(FPS)
        #process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                BurnSound.stop()
                running=False
                SourceFileWriting()
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if  x>=490 and x<=WIDTH and y>=10 and y<=110:# Continue
                    BurnSound.stop()
                    if Pause():
                        pass
                    elif Pause() == False:
                        running=False
            if event.type == pygame.MOUSEMOTION:
                x = event.pos[0]
                y = event.pos[1]
                MouseMotion = True
            else:
                MouseMotion = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            BallAcc.x = -Player_Accel
            rotate = True
        if keys[pygame.K_RIGHT]:
            BallAcc.x = Player_Accel
            rotate = True
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            BallAcc.x = 0
            rotate = False

        #update
        GoUp()
        if checkAbove():   #if a tile has went up
            Player_Score+=1
            if BallOnPower and PowerUp["Kind"]==PowerUpKinds["Scorex2"]:
                Player_Score+=1
            if BallOnPower:
                PowerUpTime+=1
            if checkAbovePower():
                PowerUpControl+=1
            if Player_Score >= Player_High_Score:
                ScoreColor=RED
                Player_High_Score = Player_Score
                HighScoreReachingVar+=1


        Laser["yPos"] += Laser["speed"]

        BallAcc.x += BallVel.x * Player_Fric
        BallVel += BallAcc
        BallPos += BallVel + 0.5 * BallAcc

        PowerUp["xPos"]+=3


        if BallPos.x>PowerUp["xPos"]-100 and BallPos.x<PowerUp["xPos"] + 100  and BallPos.y>PowerUp["yPos"] -10 and BallPos.y<PowerUp["yPos"] + 10:    #when ball gets a power
            BallOnPower=True


        if Player_Score%10==0:
            Laser_Speed+=0.01
        if PowerUpTime==5:
            PowerUpTime=0
            BallOnPower=False
            PowerUpReset()
        if PowerUpControl==5 and BallOnPower==False:
            PowerUpControl=0
            PowerUpReset()
        if PowerUpControl==5 and BallOnPower:
            PowerUpControl-=1

        if BallPos.x > WIDTH: #the ball comes back
            BallPos.x = -141
        if BallPos.x < -141:    #the ball comes back
            BallPos.x = WIDTH

        if PowerUp["xPos"] > WIDTH:    #the ball comes back
            PowerUp["xPos"] = 0

        if CheckTouch():  #if the ball is touching a tile
            if BallOnPower and PowerUp["Kind"]==PowerUpKinds["FieldRemove"]: #On Field remove power
                BallVel.y = 0
                fieldVel = 10
                Laser["yPos"]=0
            else:
                BallVel.y = 0
                fieldVel=0
        else:
            BallVel.y = 0
            fieldVel = 10

        if BallOnPower and PowerUp["Kind"]==PowerUpKinds["SpeedUp"]:
            Player_Accel = 0.8
        else:
            Player_Accel = 0.55

        if BallOnPower and PowerUp["Kind"]==PowerUpKinds["LaserStop"]:
            Laser["yPos"]=0
            RED=WHITE

        if CheckTouchPower()==False and checkAbovePower()==False:
            PowerUp["yPos"] +=  10
        if BallPos.y == HEIGHT:  #the ball comes back to y=0
            BallPos.y = 0
        if Laser["yPos"] == HEIGHT: #the laser comes back to y=0
            Laser["yPos"] = 0
        if fieldVel == 10 :   #moving the laser based on the fileds
            Laser["yPos"] -= 10
        if Laser["yPos"]<=0:  #watch out so the laser doesn't go out of the screen
            Laser["yPos"]=0
        if Laser["yPos"] >= BallPos.y + 15 and Laser["yPos"] < BallPos.y+50:  #the laser is almost catching the ball
            Player_Fric=-0.2
            Laser["speed"]=0.5
            LaserChangeVar+=3
            RED=(255,LaserChangeVar,0)
            if running:
                BurnSound.play()
        else:
            if Grass:
                Player_Fric=-0.05
            elif Ice:
                Player_Fric=-0.03
            Laser["speed"]=Laser_Speed
            if BallOnPower and PowerUp["Kind"]==PowerUpKinds["LaserStop"]:
                pass
            else:
                RED=(255,0,0)
                #Laser["L_Color"]=RED
            LaserChangeVar=0
            BurnSound.stop()
        if Laser["yPos"] > BallPos.y + 50:
            if GameOver() == False:
                running=False
            elif GameOver():
                Player_Money += Player_Score
                resetGame()

        #render
        screen.fill(BLACK)
        screen.blit(backG,(0,0))

        for printing in range (0,5): #printing fields
            DrawField(printing, field[printing]["yPos"],ColorOfFields)
        DrawLaser(Laser["xPos"],Laser["yPos"],Laser["L_Width"],RED)
        drawBall(BallPos.x,BallPos.y,rotate)
        DrawScore(Player_Score)
        if HighScoreReachingVar>0 and HighScoreReachingVar<=5:
            texts("KEEP GOING! You Reached your highscore!",25,100,30,(252,11,107),"Auth")
        screen.blit(PauseButton,(490,10))
        if BallOnPower==False:
            drawPowerUp(PowerUp["xPos"],PowerUp["yPos"])
        if BallOnPower:
            if PowerUp["Kind"]==PowerUpKinds["SpeedUp"]:
                texts("Speeding Up!!!",130,200,70,BLUE,"Auth")
            elif PowerUp["Kind"]==PowerUpKinds["FieldRemove"]:
                texts("Falling!!!",200,200,70,BLUE,"Auth")
            elif PowerUp["Kind"]==PowerUpKinds["Scorex2"]:
                texts("Score X ",130,200,70,BLUE,"Auth")
                texts("2 ",370,200,70,BLUE,"San")
                texts(" !!!",410,200,70,BLUE,"Auth")
            elif PowerUp["Kind"]==PowerUpKinds["LaserStop"]:
                texts("Goodbye Laser!!!",70,200,70,BLUE,"Auth")   #bliting the power txts
        if Player_Score<6:
            screen.blit(TutorialBlack , (51,521))
            screen.blit(Tutorial , (50,520))

            #screen.blit(pygame.image.load("Tutorial.png") , (51,521))
        if MouseMotion:
            screen.blit(CursorImage,(x,y))
        pygame.display.flip()
    Player_Money += Player_Score
    resetGame()
def Pause():
    PauseRunning = True
    while PauseRunning:
        for event in pygame.event.get():
            clock.tick(30)
            if event.type == pygame.QUIT:
                PauseRunning = False
                SourceFileWriting()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if  x>=90 and x<=220 and y>=373 and y<=426:# Continue
                    return True
                elif x>=365 and x<=525 and y>=373 and y<=424:#MainMenu
                    return False

        screen.fill(BLACK)
        screen.blit(PauseWindow,(50,231))
        x,y = pygame.mouse.get_pos()
        screen.blit(CursorImage,(x,y))
        pygame.display.flip()
def menu():
    menuRunning = True
    global StartButton
    global backG
    global MenuBackG
    while menuRunning:
        for event in pygame.event.get():
            clock.tick(30)
            if event.type == pygame.QUIT:
                menuRunning = False
                SourceFileWriting()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>=180 and x<=390 and y>=210 and y<=436:
                    LoadBalls(BallUsing)
                    LoadBackG(BackGroundUsing)
                    RunGame()
                elif x>=500 and x<=WIDTH and y>=10 and y<=90:
                    SettingsPage()
                elif x>=220 and x<=370 and y>=410 and y<=560:
                    ShoppingPage()
                elif x>=10 and x<=90 and y>=10 and y<=90:
                    InfoPage()

        screen.blit(MenuBackG,(0,0))
        screen.blit(StartButton,(185,210))
        screen.blit(SettingButton,(WIDTH-100,10))
        screen.blit(InfoButton,(10,10))
        screen.blit(CustomizePic,(225,415))
        texts("Money: "+str(Player_Money),240,10,25,(210,210,210),"San")
        texts("High Score: "+str(Player_High_Score),220,60,25,(210,210,210),"San")
        x,y = pygame.mouse.get_pos()
        screen.blit(CursorImage,(x,y))
        pygame.display.flip()

menu()
SourceFileWriting()
pygame.quit()
