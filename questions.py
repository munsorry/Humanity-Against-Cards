'''
This program is for my personal game, 'Humanity Against Cards'.
It will be imported, but this program just collects and assembles the questions.
This game will work opposite to Cards Against Humanity
'''


import random

def collectQuestions(questions):
    user = input("Enter a funny question. Enter 'q' to quit. ")

    if user == 'q':
        print("Program terminated.")
        return questions
    
    while user != 'q':
        if user in rawQuestions:
            print("Already entered.")
            collectQuestions(rawQuestions)            
            
        else:
            questions.append(user)
            print("Current Answers:")
            print()
            print(rawQuestions)
            collectQuestions(rawQuestions)

    print(questions)
    return questions

#collectQuestions(rawQuestions)
    
def createQuestionsDeck():
    rawQuestions = ['In its new tourism campaign, Detroit proudly proclaims it has finally eliminated __________.', 'Genshin Impact would be so much better if it only had __________ in it.', 'The __________ to gay pipeline is insane, man.', 'What does your mother prefer in bed?', 'Ah yes, __________. Good down to the last drop.', "What's the worst thing to find in your Chinese food?", '__________: Kid-tested, mother-approved.', "What ended my cat's last relationsip?", 'Michael Jackson WISHES he had __________ ', '__________? Jesus could never.', "__________? There's an app for that.", '__________ only gets better with age.', "What's up with Dad?", 'In the distant future, historians will fight over the morality of Twitter\'s "hot takes" on __________.', 'Being a nudist is so hard when you have to deal with the incessant __________.', 'I just __________. Can I get a hug?', 'After the accident, Sean could never see __________ the same.', "I'm blind to racism! I don't care if you're black, brown, white, or __________.", 'Times were simpler when __________ was/were free.', 'Life was so simple before those damn lizard-brains figured out how to __________.', 'I love it when my wife decides to just shout "__________" in the middle of our family get-together.', 'Art is so easy. All you need to do is __________.', 'Grandma? Is that you __________?', "Offensive? My humour?! No way. It's not my fault you're so sensitive around __________.", "A blowjob would be nice, but __________? Now that's what I'm talking about.", "After meeting the toddler next door, I just can't stop thinking about __________.", "I could really go for some __________ right now. It's been a long 15 minutes at work", 'And the Academy Award for frutiest bitch has got to go to...', "What's a girl's best friend?", "Lifetime supply of food, or __________? That's a tough one.", '__________  is like 85% of my impulse control.', "__________? That's not what your mother said last night, dear.", "Your grades have gone down, Sarah. Iit's time we start talking about the __________.", '__________ gets me off like nothing else nowadays.', "Japan's birth-rate is plummeting, but don't worry. __________ is here to help.", "Don't get into __________. Worst mistake of my life.", 'JK Rowling sponsoring __________ sounds like a great time.', 'Not even the amazing power of Flex-Tape can keep me away from getting my grubby little hands all over __________.', "What's that smell in the back of the house, Sharon?", "Sorry, everyone. I've decided to come out as __________.", "I can't hide it anymore, guys. I am addicted to __________.", "Who's more emo, a literal emo or _________?", 'For my next trick, I will finally get a __________.', 'The class field trip was fun, aside from the __________, at least.', "The President may reign supreme and I'm all for it, but in this house, only __________ can make me interested enough to get up before 9:30 AM in the morning.", 'Something about playing League of Legends while __________ makes a man really just decide to end it all.', "__________. That's the tweet.", 'Superman would be so much more interesting if, instead of flying or shooting lasers out of his eyes, he could just __________.', 'Hey sexy. Got anymore of that __________?', 'The government wants to hide the __________. It makes kids too powerful for their own good.', 'The U.S. saw __________ in the Middle East and went "Oh nah. Get the bombs."', "When I'm a billionare, I'm going to erect a 50-foot statue of __________ outside my house, and no one can stop me.", 'When all else fails, I know I can count on __________ to get me going.', 'My wife cheated on me for __________. I have only myself to blame.', 'Roses are red, violets are blue. You like __________, and your mother still gave birth to you?', 'I never truly understood __________ until I tried. Now I am HOOKED.', "I don't need games to keep me entertained. I have __________.", 'I do not deserve to pay rent when I already have to deal with __________ in my apartment, Mr. Landlord!', 'Are my parents hiding a __________ from me?', "It's just something about white people that makes mankind __________.", 'Obama would, without a doubt, wage a war over __________.', 'Lil Nas was a Lil Nasty for this one: __________', 'My auntie bought __________ back from Mexico. Tasted great.', 'Tsunderes. Catgirls. My step-sister. The literal doormats. Long ago, the 4 overrated waifu tropes were at peace, all equally bad. Then, everything changed when the __________ attacked.', "Why can't I sleep at night? All I had for dinner was __________...", 'What do you mean __________ hurts? I was able to put it in me just fine.', "__________, but naked. Now that's what I'm talking about.", 'This pandemic has caused a massive shortage in _________.', "My girlfriend told me she's really into _________. I thought I knew what I was getting into. I did not.", 'Being a superhero is no fun unless you have _________ by your side.', 'The Russian Government really peaked when they came up with _________.', 'In New York City, people could literally get away with _________ on the subway and no one would say a damn thing.', "80-year olds might not get a lot of action at night, but that's okay. If they're ever in the mood they can always rely on _________ for some fun.", "I got 99 problems, but _________ isn't one. I've mastered that a long time ago.", "Sometimes I just want to eat _________. Don't judge me.", 'War might be bloody, but hey. At least in the end we can all relish in the _________ afterwards.', "Not to be a simp but if a girl had _________, I'd literally hand over my rights to her.", 'I wish my mom taught me how to _________ before I went to college. The boys in the dorm were ashamed of my lack of knowledge on the topic.', 'Just saw my Physics professor dancing to _________ in the lounge room. Might as well just drop the course now.', 'White people be like "Yo _________ is FIRE" and it\'s the stalest shit I\'ve ever seen. We\'re all over it, Sally, _________ is nothing new. ', 'Sugarmommies are so overrated. I get money from an actually reliable source, like _________.', "Nnngh... not so hard, dad. It's my first time trying out _________.", "My father went out to get _________ from the store. I'm sure he'll be back in a few minutes.", 'In the darkest pits of Hell, sinners must endure _________ for all of eternity. Serves them right.', 'I want to consider myself a wholesome individual but my mother really makes me want to _________ sometimes.', 'Imagine Hatsune Miku but _________. Thoughts?', "God...that weatherman could report about _________ and I'd still give him my full attention.", 'I dropped out of college for _________. Smartest decision of my life.', "Bill Gates might have a lot of money, but does he have a mastery of _________ the way I do? That's what I thought, so who's really the rich one here?", 'The blind date was rather lackluster at first, but once I found out he and I both had a shared passion for _________ I was ready to marry him on the spot. ', 'Life would be so much more fun if cats could _________ from time to time.', "I'm not like other boys. I actually _________.", "_________ might get me a warrant for arrest, but it'll be worth it.", "Ah yes. The 3 Golden G's in life: Gacha, Gay People, and G-_________.", 'I never really fit in while I was in high school. So I made a club for _________ and immediately got mad bitches.', "Hey baby. Come back to my place why don't you? I've got plenny'a __________ that ya might like.", 'Why did my cousin just walk in, __________ all over my couch, and leave?', "I'm not a big fan of __________. I actually want to be able to sleep at night with a guilt-free conscience.", "Listen son. If you want to get into marijuana I can not stop you. Just please. For your sake. For my sake. For your mother's sake. For God Almighty's sake. Steer clear of __________.", 'My life is a vicious cycle of starving myself in exchange for __________. Help.', 'I am NOT sexist! I love a girl with __________.', 'My boss really wanted to be honest with me. He said that he started developing feelings for me after I was __________ in the meeting last week. ']
    questions = []
    for question in rawQuestions:
        questions.append(question.replace("__________", "[BLANK]"))
    questions2 =[]
    for question in questions:
        questions2.append(question.replace("_________", "[BLANK]"))
        
    random.shuffle(questions2)
    
    return questions2

#collectQuestions(rawQuestions)
createQuestionsDeck()


