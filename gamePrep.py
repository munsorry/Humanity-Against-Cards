'''
this program is to generate 7 hands so I can privately message it to other
players who are participating in the game so that the answers
doesn't appear in the main program's stream.

'''
import random
import answers
import questions

questions = questions.createQuestionsDeck()
answers = answers.createAnswersDeck()

print()
print("--------------------------------\
-----------------------")
print("Pick one answer for each round's question.")
print()

for i in range(7): #7 questions per round
    hand = []
    cardNum = 0
    print("Hand for question", str(i+1), "of this round" + ":")
    while (len(hand) < 5): #5 cards per hand, per question
        ranAn = random.choice(answers)
        if ranAn not in hand:
            cardNum +=1
            hand.append(ranAn)
            print("||Card",str(cardNum) + ")",'"' + hand[cardNum-1] + '"||')
    print()
    print()
    print()

    
