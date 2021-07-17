import random
import answers
import questions


questions = questions.createQuestionsDeck()
answers = answers.createAnswersDeck()

scores = {} # {playerName : Total Score so far}

def runBloopers():
    text = "This game was so simple in theory, that is- in my head. You just take some goddamn questions and answers and distribute them amongst people, then have them grade each other's responses. Little kids can understand this game. But actually automating it into Python code...took a while. I'd say I put about 15 hours into this very simple game, which works using 3 different program files and 6 different functions to automate and properly randomize question and answer generation. Really goes to show you how hard coding even simple things can be. Still, thanks for participating in this project of mine. Because it's NSFW I can't put it on my resume though lol."
    print(text[0:83])
    print(text[83:166])
    print(text[167:250])
    print(text[251:335])
    print(text[336:414])
    print(text[416:498])
    print(text[498:579])
    print(text[580:])
    return()
    
def cleanNumberInput(string):
    realInput = ''
    for c in str(string):
        if c in '0123456789.':
            realInput += c
            realNumber = float(realInput)
        else:
            cleanNumberInput(string[1:])
    return realNumber

def clearShell(lines = 35):
    for i in range(lines):
        print()
    return()

def startGame():

    clearShell()
    print("Be sure to run gamePrep.py before starting.")
    print()
    print("Welcome to Humanity Against Cards! In this game, players")
    print("vote on a certain player's answer to a random question. They")
    print("are each given random answers - they DON'T make up their own! ")
    print("It's your job to come up with the funniest responses to win! ")
    print()
    print("Best of luck.")
    print()
    print("...")
    print("...")
    clearShell(1)
    print("Preparing Game.")
    clearShell(2)

    doubleCheck = input("Before we start, has Momo given everyone their hands" +
                        " with gamePrep.py? ") 
    if "y" not in doubleCheck.lower():
        print()
        print("Please assign players their hands FIRST, then start the game.")
        return(0)
#This is a check to ensure I've held the
    clearShell(2)
    print("NOT including Momo,")
    numPlayers = input("How many players are playing? ")
    while cleanNumberInput(numPlayers) <=2.99999999: 
        numPlayers = input("Need at least 3 other people. How many will play? ")
    numP = (int(round(cleanNumberInput(numPlayers),1)))

    playerList = []
    for i in range(numP):
        name = input("What is player "+str(i+1)+ "'s name? Enter:  ")
        while name == '':
            name = input("Enter valid name: ")
        scores[name] = 0
        playerList.append(name)
 
    print("Please remember your player numbers.")
    print()
    print("A round consists of each player answering 7 questions. How")
    x = int(round((15*7*(numP+1)/60)+0.49, 2))
    print("many rounds will this game consist of? Each round takes about", x)
    print("minutes, so choose accordingly.")
    print()
    
    numRounds = input("How many rounds will you play? ")
    currentRound = 0
    numR = int(numRounds)

    clearShell(2)
    print("The game will now begin.")
    print()
# - - - - - - - - - - - - - each round begins here - - - - - - - - - - - - -
    for i in range(numR):
        print("Round", str(i + 1), "will now begin.")
        clearShell(2)

        wait4QstnGnrtn = input("Generated. Ready to begin round? ")
        while "y" not in wait4QstnGnrtn:
            wait4QstnGnrtn = input("Generated. Ready to begin round? ")
            
        clearShell(2)
        currentPlayer = 0
# - - - - - - - - - each player's turn within the round begins here - - - - - -
        for player in scores:
            currentPlayer +=1
            questionsAskedThisRound = []
            questionsAsked = 0
          
            while(questionsAsked < 7): #for the 7 questions:
          
                ranQ = random.choice(questions)
                if ranQ not in questionsAskedThisRound:
                    print("~~~~~~~~~~")
                    print("Round:",currentRound+1)
                    print("Question",str(questionsAsked+1),"for\
 Player", str(currentPlayer)+":")
                    questionsAsked +=1
                    print("~~~~~~~~~~")
                    print()
                    print(ranQ)
                    print()
                    questionsAskedThisRound.append(ranQ)
                    playerResponse = input("Answer: ")
                    while playerResponse == '':
                        print("Enter a valid answer from the player's hand: ")
                        playerResponse = input("Answer to the above question: ")            
#Start grading the response.
                for difPlayer in range(numP-1):
                    print("Players other than " + str(currentPlayer)
                          + ", how funny was this response?")
                    addScore = input("Give this answer a score\
from 5 to 10. Decimals allowed. ")
                    while addScore == '':
                        print("Please enter a VALID numerical response")
                        addScore = input("Give this answer a score from 5 to\
 10.")
                    while float(addScore) > 10 or float(addScore) < 5:
                        print()
                        print("Please enter a VALID numerical response")
                        addScore = input("Give this answer a score from 5 to\
 10.")

                        
                    value = cleanNumberInput(float(addScore))
                    scores[player] += value
                    print()
                print("Player", str(currentPlayer)+"'s","Score:", scores[player])
                clearShell(6)
            if currentPlayer > numP:
                currentPlayer -= numP
            print("Next Player Up: Player",currentPlayer+1)
            print("Current Round Number:", currentRound)
            clearShell(3)

        currentRound +=1
        top1 = 0
        top2 = 0
        for i in scores:
            if scores[i] > top1:
              top1 = scores[i]
              firstPlace = i
        print("~~~~~~~~~~")
        print("The winner of this round is:", firstPlace, "with a score of:")
        print("->", str(top1)+".")
        print("~~~~~~~~~~")
        print()
        
        for i in scores:
            if scores[i] < top1 and scores[i] > top2:
                top2 = scores[i]
                secondPlace = i 

        print("~~~~~~~~~~")
        print("In second place is:", secondPlace, "with a score of:")
        print("->", str(top2)+".")
        print("~~~~~~~~~~")
        print()
            
    print()
    print("The rounds are now over, and the game is complete.")

        

    print("Congratulations to everyone, and thank you for playing.")
    print()
    playAgain = input("Play again? Yes to restart, or hit Enter to quit: ")
    if 'y' in playAgain.lower() and len(playAgain) < 4:
        startGame()
    if playAgain == "":
        print("Thank you for playing.")
        return(0)
    else:
        balls = input("Care to read about the creation of this game? ")
        if balls.lower()[0] == "y":
            runBloopers()
        else:
            return(0)
          

#Here, I need to go to gamePrep.py and make 7 "hands" for the player.
startGame()



    
