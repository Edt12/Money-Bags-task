

import pygame
import random

pygame.init()
screen_width = (1200)
screen_height = (700)
screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
pygame.display.set_caption("Word Check Game")
clock = pygame.time.Clock()
background= pygame.image.load("Jungle.webp")
#defining colours
black=(0,0,0)
white=(255,255,255)
#finding word to display from list
words=("adduct","absurd","acquit","adjust","badger","bangle","becalm","bicker","bought","bounce","bowler","branch",
     "bright","calmer","canter","carpet","catkin","chapel","choral","common","damson","dancer","deacon","depart",
     "deputy","detail","dinghy","dismay","dollar","earwig","eating","fabric","facing","factor","family","figure",
     "firmly","flower","flying","foiled","garlic","garnet","gasped","gerbil","golden","guitar","halved","harmed",
     "hearty","hockey","housed","lawyer","learnt","lizard","longer","magnet","magpie","manger","marble","neatly")
currentWord=random.sample(words,1)#selects random word from list 1 is how many to select
currentWord=str(currentWord)
currentWord=currentWord.replace("[","")#gets rid of brackets and apostraphes because strings from random sample command  are bracketet
currentWord=currentWord.replace("]","")#example ['lawyer']
currentWord=currentWord.replace("'","")
#setting text font and creating on screen letters
font=pygame.font.Font("freesansbold.ttf",100)#font=font,Font=size
letter1=font.render("_",True,black)#""=text,true= if antialiasing or not,black = colour
letter2=font.render("_",True,black)
letter3=font.render("_",True,black)
letter4=font.render("_",True,black)
letter5=font.render("_",True,black)
letter6=font.render("_",True,black)
#creates a surface for the text to go on to for each letter
letter1Rect=letter1.get_rect()
letter2Rect=letter2.get_rect()
letter3Rect=letter3.get_rect()
letter4Rect=letter4.get_rect()
letter5Rect=letter5.get_rect()
letter6Rect=letter6.get_rect()
#creates font for text input box
userFont=pygame.font.Font("freesansbold.ttf",50)
#creates font for things other than the text box
generalSmallFont=pygame.font.Font("freesansbold.ttf",30)
#defining user text e.g what user types in
userText=""
#creates a rect for a user input box
Inputrect=pygame.Rect(screen_width/2,screen_height/2+100,25,50)#x,y,width,hieght
#creating a sign at the below the text box to tell the user to type in only lower case letters
lowercaseSign=generalSmallFont.render("Please type in only lowercase letters",True,black)
lowercaseSignRect=lowercaseSign.get_rect()
#making a limit to number of guesses and creating guess number on screen
guessNum=0
guessNumgraphic=font.render(str(guessNum),True,black)#first updating graphic
guessNumgraphicRect=guessNumgraphic.get_rect()

guessNumgraphic2=font.render("/10",True,black)#second static one
guessNumgraphic2Rect=guessNumgraphic2.get_rect()

guessSign=generalSmallFont.render("Guesses Remaining",True,black)#creating a sign to say what the numbers mean
guessSignRect=guessSign.get_rect()
#creating a win or lose graphic
winMessage=generalSmallFont.render("",True,black)
winMessageRect=winMessage.get_rect()

WinChecker =0#goes up every time a letter is pressed totrack whether user has guessed all the letters
#creating variable to check whether a letter has been guessed
letter1guessed=False
letter2guessed=False
letter3guessed=False
letter4guessed=False
letter5guessed=False
letter6guessed=False

while True:
    halfScreenwidth=screen_width/2
    halfScreenheight=screen_height/2


    #postions text on screen
    letter1Rect.center = (halfScreenwidth   ,halfScreenheight)
    letter2Rect.center = (halfScreenwidth+80,halfScreenheight)
    letter3Rect.center = (halfScreenwidth+160, halfScreenheight)
    letter4Rect.center = (halfScreenwidth+240, halfScreenheight)
    letter5Rect.center = (halfScreenwidth+320, halfScreenheight)
    letter6Rect.center = (halfScreenwidth+400,halfScreenheight)
    guessNumgraphicRect.center= (halfScreenwidth-300,halfScreenheight)
    guessNumgraphic2Rect.center=(halfScreenwidth-150,halfScreenheight)
    guessSignRect.center=(halfScreenwidth-200,halfScreenheight-100)
    winMessageRect.center=(halfScreenwidth,halfScreenheight-200)
    lowercaseSignRect.center=(halfScreenwidth,halfScreenheight+200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            #defining key presses for letters in text box
            if event.key == pygame.K_a:
                userText = "a"

            if event.key == pygame.K_b:
                userText = "b"

            if event.key == pygame.K_c:
                userText = "c"

            if event.key == pygame.K_d:
                userText = "d"

            if event.key == pygame.K_e:
                userText = "e"

            if event.key == pygame.K_f:
                userText = "f"

            if event.key == pygame.K_g:
                userText = "g"

            if event.key == pygame.K_h:
                userText = "h"

            if event.key == pygame.K_i:
                userText = "i"

            if event.key == pygame.K_j:
                userText = "j"

            if event.key == pygame.K_k:
                userText = "k"

            if event.key == pygame.K_l:
                userText = "l"

            if event.key == pygame.K_m:
                userText = "m"

            if event.key == pygame.K_n:
                userText = "n"

            if event.key == pygame.K_o:
                userText = "o"

            if event.key == pygame.K_p:
                userText = "p"

            if event.key == pygame.K_q:
                userText = "q"

            if event.key == pygame.K_r:
                userText = "r"

            if event.key == pygame.K_s:
                userText = "s"

            if event.key == pygame.K_t:
                userText = "t"

            if event.key == pygame.K_u:
                userText = "u"

            if event.key == pygame.K_v:
                userText = "v"

            if event.key == pygame.K_w:
                userText = "w"

            if event.key == pygame.K_x:
                userText = "x"

            if event.key == pygame.K_y:
                userText = "y"

            if event.key == pygame.K_y:
                userText = "z"


            if event.key==pygame.K_RETURN and guessNum <10 and userText!=currentWord[0] and userText!= currentWord[1] and userText != currentWord[2] and userText!=currentWord[3] and userText !=currentWord[4] and userText!=currentWord[5] and userText!="":
                guessNum+=1
                guessNumgraphic=font.render(str(guessNum),True,black)#updates the score counter

            if event.key== pygame.K_RETURN and currentWord[0] ==userText and guessNum<10 and letter1guessed==False:
                letter1 = font.render(userText, True, black)
                WinChecker+=1
                letter1guessed=True

            if event.key== pygame.K_RETURN and currentWord[1]==userText and guessNum<10 and letter2guessed==False:
                letter2 = font.render(userText, True, black)
                WinChecker+=1
                letter2guessed=True

            if event.key == pygame.K_RETURN and currentWord[2] ==userText and guessNum<10and letter3guessed==False:
                letter3 = font.render(userText, True, black)
                WinChecker+=1
                letter3guessed=True

            if event.key== pygame.K_RETURN and currentWord[3] ==userText and guessNum<10 and letter4guessed==False:
                letter4 = font.render(userText, True, black)
                WinChecker+=1
                letter4guessed=True

            if event.key== pygame.K_RETURN and currentWord[4]==userText and guessNum<10and letter5guessed==False:
                letter5 = font.render(userText, True, black)
                WinChecker+=1
                letter5guessed=True

            if event.key== pygame.K_RETURN and currentWord[5] ==userText and guessNum<10and letter6guessed==False :
                letter6 = font.render(userText, True, black)
                WinChecker+=1
                letter6guessed=True

            if event.key== pygame.K_BACKSPACE:
                userText = userText[:-1]#tells user text to go del1ete last character this is needed as unicode does not have a backspace function

            if textSurface.get_width()>20:#limits text box to only one character
                userText=userText[:-1]

            if  letter1guessed==True and letter2guessed==True and letter3guessed==True and letter4guessed==True and letter5guessed==True and letter6guessed==True:
                winMessage=generalSmallFont.render("Congratulations you win",True,black)

            if letter1guessed==False and letter2guessed==False and letter3guessed==False and letter4guessed==False and letter5guessed==False and letter6guessed==False:
                winMessage=generalSmallFont.render("Game over you lost!",True,black)



    pygame.draw.rect(screen, white, Inputrect)#draws text box
    textSurface=userFont.render(userText,True,black)
    screen.blit(textSurface,(Inputrect.x+5,Inputrect.y+5))#renders text surface on Input rect but slightly to side to stop overflow-generates rectangle whever it is typed
    Inputrect.w = max(20, textSurface.get_width()+10)

   #generates letters on screen by updating the screen
    screen.blit(letter1,letter1Rect)
    screen.blit(letter2,letter2Rect)
    screen.blit(letter3,letter3Rect)
    screen.blit(letter4,letter4Rect)
    screen.blit(letter5,letter5Rect)
    screen.blit(letter6,letter6Rect)
    screen.blit(guessNumgraphic,guessNumgraphicRect)
    screen.blit(guessNumgraphic2,guessNumgraphic2Rect)
    screen.blit(guessSign,guessSignRect)
    screen.blit(winMessage,winMessageRect)
    screen.blit(lowercaseSign,lowercaseSignRect)
    pygame.display.update()  # keeps window open
    screen.blit(background,(0,0))#generates background
    #sets framerate
    clock.tick(60)


