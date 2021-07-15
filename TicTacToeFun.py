import sys
import msvcrt
import time
import random
import math
class TimeoutExpired(Exception):
    pass

#Checking the different cases of win or loss
def checkwin(mlt1):
    i=1
    while i<=3:
        if mlt1[1+(i-1)*3][1+(1-1)*4]!=" " and mlt1[1+(i-1)*3][1+(1-1)*4]==mlt1[1+(i-1)*3][1+(2-1)*4]==mlt1[1+(i-1)*3][1+(3-1)*4]:
            if mlt1[1+(i-1)*3][1+(1-1)*4]=="X":
                print("You win....For this time.\nBeware next time, mortal. Dareth thou challenge my might again?")
            else:
                print("You lost.\nAwww, always can try again y'know :)")
            wanna=input("To play again, enter any input. To exit, enter N:")
            if wanna=="N" or wanna=="n":
                print("\n\nHa! Resistance is futile.\nLook upon my works ye mighty and despair")
                print("\n\nUgh nevermind that guy...\n\nTHANK YOU FOR PLAYING!\n\n")
                sys.exit()
            else:
                letsplay()
        
        elif mlt1[1+(1-1)*3][1+(i-1)*4]!=" " and mlt1[1+(1-1)*3][1+(i-1)*4]==mlt1[1+(2-1)*3][1+(i-1)*4]==mlt1[1+(3-1)*3][1+(i-1)*4]:
            if mlt1[1+(1-1)*3][1+(i-1)*4]=="X":
                print("You win...For this time.\nBeware next time, mortal. Dareth thou challenge my might again?")
            else:
                print("You lost.\nAwww, always can try again y'know :)")
            wanna=input("To play again, enter any input. To exit, enter N:")
            if wanna=="N" or wanna=="n":
                print("\n\nHa! Resistance is futile.\nLook upon my works ye mighty and despair")
                print("\n\nUgh nevermind that guy...\n\nTHANK YOU FOR PLAYING!\n\n")
                sys.exit()   
            else:
                letsplay()
        i+=1
    while True:
        if (mlt1[1][1]!=" " and mlt1[1][1]==mlt1[4][5]==mlt1[7][9]) or (mlt1[1][9]!=" " and mlt1[1][9]==mlt1[4][5]==mlt1[7][1]):
            if mlt1[4][5]=="X":
                print("Das nicht so gut")
                print("You Win.....For this time.\nBeware next time, mortal. Dareth thou challenge my might again?")
            else:
                print("You lost.\nAwww, always can try again y'know :) ")
            wanna=input("To play again, enter any input. To exit, N:")
            if wanna=="N" or wanna=="n":
                print("\n\nHa! Resistance is futile.\nLook upon my works ye mighty and despair")
                print("\n\nUgh nevermind that guy...\n\nTHANK YOU FOR PLAYING!\n\n")
                sys.exit()
            else:
                letsplay()
        else:
            break


#Main play function: To choose game settings and interact with the game. Checkwin function is used to check status after each iteration/play
def letsplay():
    while True:
        diffinput=int(input("\n\nSelect Game difficulty level.\nEnter 1 for Easy (too easy), 2 for Medium, 3 for ahem...A c c e p t a b l e :"))
        if diffinput==1:
            diffsetting=5
            break
        elif diffinput==2:
            diffsetting=4
            break
        elif diffinput==3:
            diffsetting=3
            break
        else:
            print("Invalid difficulty level.\nPlease enter valud difficulty level: 1, 2, or 3")
    print("Now enter any key to start the game.\n\n\nBe ready, the sands of time flow fast... :")
    msvcrt.getwche()
    
    #Creating the Tic-Tac-Toe play-matrix (with lines)
    mlt1=[]
    for i in range(3):
        for j in range(2):
            l1=[' '*3,' ',' '*3,'|',' '*3,' ',' '*3,'|',' '*3,' ',' '*3]
            mlt1.append(l1)
            errhandl11=j+1
            errhandl11+=1
        if i>1:
            break 
        l1=['_'*3,'_','_'*3,'|','_'*3,'_','_'*3,'|','_'*3,'_','_'*3]
        mlt1.append(l1)
    l1=[' '*3,' ',' '*3,'|',' '*3,' ',' '*3,'|',' '*3,' ',' '*3]
    mlt1.append(l1)
    for i in range(len(mlt1)):
        print("".join(mlt1[i]))
    playcount=[]
    
    while True:
        #Checking win/loss status
        checkwin(mlt1)
        
        #Checking if all positions exhausted, if yes, then game over
        
        if len(playcount)>=9:   
            print("Game Over...\nDas nicht so gut")
            wanna=input("To play again, enter any input. To exit, enter N:")
            if wanna=="N" or wanna=="n":
                print("\n\nHa! Resistance is futile.\nLook upon my works ye mighty and despair")
                print("\n\nUgh nevermind that guy...\n\nTHANK YOU FOR PLAYING!\n\n")
                sys.exit()   
            else:
                letsplay()
        
        cheat=0  #initializing cheat count for this attempt
        while True:
            
            #Timed input according to game difficulty setting selected
            try:
                prompt1="You have %d seconds...Enter row no.: " % diffsetting
                prompt2="\nYou have %d seconds...Enter column no. :" % diffsetting
                n1 = input_with_timeout(prompt1, diffsetting, gamesetting)
                n2= input_with_timeout(prompt2, diffsetting, gamesetting)
                
            except TimeoutExpired:
                print("\nSorry, times up")
                [n1,n2]=['\0','\0']
                [n1,n2]
            else:
                pass
            print("\n")
            if [n1,n2]==['\0', '\0']:
                print("Game Over...\nDas nicht so gut")
                wanna=input("To play again, enter any input. To exit, enter N:")
                if wanna=="N" or wanna=="n":
                    print("\n\nHa! Resistance is futile.\nLook upon my works ye mighty and despair")
                    print("\n\nUgh nevermind that guy...\n\nTHANK YOU FOR PLAYING!\n\n")
                    sys.exit()   
                else:
                    letsplay()
                    
            #Checking validity of input
            elif [n1,n2] in playcount or n1 not in range(1,4) or n2 not in range(1,4):
                print("Um, that position is already occupied or unavailable. Please enter another position. %d tries left" % (2-cheat) )
                
                #Checking if player entering wrong input just to get more time to think. If more than limit of wrong inputs, game over.
                
                if cheat<2:
                    cheat+=1
                    continue
                else:
                    print("Game Over...\nDas nicht so gut")
                    wanna=input("To play again, enter any input. To exit, enter N:")
                    if wanna=="N" or wanna=="n":
                        print("\n\nHa! Resistance is futile.\nLook upon my works ye mighty and despair")
                        print("\n\nUgh nevermind that guy...\n\nTHANK YOU FOR PLAYING!\n\n")
                        sys.exit()
                    else:
                        letsplay()

            break  
            
        #Appending input position to list of occupied positions if it is valid
        #Also inserting player's move to play-matrix
        
        mlt1[1+(n1-1)*3][1+(n2-1)*4]="X"  
        playcount.append([n1,n2]) 
        for i in range(len(mlt1)): 
            print("".join(mlt1[i]))
        checkwin(mlt1)
        input("\nPress Enter to be enthralled at my move. Me the destroyer of worlds mwahaha- :\n")
        
        #Computer's move: Randomly generated
        
        while True and len(playcount)<9:
            n1=random.randint(1,3); n2=random.randint(1,3)
            if [n1,n2] in playcount:
                pass
            else:
                mlt1[1+(n1-1)*3][1+(n2-1)*4]="O"  
                playcount.append([n1,n2]) 
                for i in range(len(mlt1)): 
                    print("".join(mlt1[i]))
                break

#For input with timeout

def input_with_timeout(prompt, timeout, gameset, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    countdowner=endtime-timer()
    print(math.ceil(countdowner), end=' ')
    while timer() < endtime:
        if msvcrt.kbhit():
            print("")
            result.append(msvcrt.getwche())
            if gameset==1:
                if result[-1] =='\r':
                    return int(''.join(result[:-1]))
            elif gameset==2:
                return int(''.join(result[:]))
        else:
            if countdowner-(endtime-timer())>=1:
                countdowner=endtime-timer()
                sys.stdout.flush()
                print(math.ceil(endtime-timer()), end=' ')
        time.sleep(0.04)
    raise TimeoutExpired


print("\n\nWELCOME! \n\nPLEASE READ THESE INSTRUCTIONS BEFORE PROCEEDING\n\n"
"-----------------------------------------------Tic Tac Toe Game(X-O Game) by Sw4pn41 V4rm4"  #Sorry, trying to avoid search results haha
"------------------------------------------------\n\nIn this 3*3 X-O grid game, you will have to select the box by specifying"
" The row and column number\nFrom (1 and 1) for top left corner, to (3 and 3) for bottom right corner\n\n"
"The rows are horizontal, and the columns vertical (if you didn't know that already smh)\nE.g.: Entering row no. as 2"
" and column no. as 3 will insert your move (X) at the middle cell to the rightmost.\n\n"
"You play against the mighty X-O champion, my Gladiatorial creation: Xenos\n\n\nNow as great as he is at the game,"
" to make things interesting,\nYou will be given only 3 seconds each to enter the row and column number.\n\nFailure"
" to do so will mean you lose the game, and will have to try again :')\n\n\n"
"--------------------------------------------------ENJOY-------------------------------------------------------------")
print("Select primary game setting:\nWhen entering row and columns, if you want your input to be taken only after you press Enter"
", then select Setting 1.\nIf you want it to be taken as soon as you press the number (don't press enter) then select Setting 2"
"\n\nSetting 2 is recommended as you will have less time (depending on difficulty level), and by the time you press enter"
"\n...you might lose"
"\nEnter 1 for Setting1 and 2 for Setting 2:")
gamesetting=int(input())
print("\n\nYou have selected Setting ", gamesetting)
gamestart=input()
letsplay()
