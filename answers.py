'''
This program is for my personal game, 'Humanity Against Cards'.
It will be imported, but this program just collects and assembles the deck.
This game will work opposite to Cards Against Humanity
'''


import random

def collectAnswers(answers):
    user = input("Enter a funny answer. Enter 'q' to quit. ")

    if user == 'q':
        print("Program terminated.")
        return answers
    
    while user != 'q':
        if user in rawAnswers:
            print("Already entered.")
            collectAnswers(rawAnswers)            
            
        else:
            answers.append(user)
            print("Current Answers:")
            print()
            print(rawAnswers)
            collectAnswers(rawAnswers)

    print(answers)
    return answers

#collectAnswers(rawAnswers)

def cleanAnswers(rawAnswers):
    answers = []
    for rawAnswer in rawAnswers:
        if '\r' in rawAnswer:
            answer = rawAnswer[0:(len(rawAnswer)-1)].lower()
            answers.append(answer)

        else:
            answers.append(rawAnswer.lower())

    return answers

    
def createAnswersDeck():
    rawAnswers = ['cockfights', "a gypsy's curse ",'granblue fantasy', 'dead parents', 'friendly fire', 'a moment of silence', 'object permanence', 'ronald reagan', 'a sausage festival', 'opposable thumbs', 'a disappointing', 'birthday party', 'an honest cop with', 'nothing left to lose', 'racially-biased sat', 'questions', 'a sassy black', 'woman', 'famine ', 'jibber-jabber', 'mathletes ', 'flesh-eating', 'bacteria', 'chainsaws for', 'hands', 'a tiny horse ', 'flying sex snakes', 'nicolas cage', 'william shatner', 'not giving a shit', 'about the third', 'world', 'child beauty', 'pageants', 'sexting my father', 'riding off into the sunset', "my girlfriend's girlfriend", 'explosions', 'an m. night', 'shyamalan plot', 'twist', 'sniffing glue ', 'shapeshifters', 'jewish people with afros', 'porn stars ', 'repressing my boner that my mom gave me', 'pedophiles', 'my really dry vagina', 'grave robbing for exp points', 'authentic mexican', 'cuisine', 'a murder most foul', 'poor people', 'her royal highness,', 'queen elizabeth ii', 'daddy issues', 'being gay', 'being born a woman', 'the donald trump', 'seal of approval', 'wiping her butt clean', 'former president', 'george w. bush', 'full frontal nudity ', 'my micro-penis', 'aids', 'my hormonal issues', "what's left of my soul", 'laying an egg', 'pictures of boobs', 'vikings and possibly my mother', 'pretending to care about gay people', 'people who are so hot for no reason', 'seducing santa for his cookies ;)', 'shame me daddy', 'getting really high to feel something', 'my oedipus complex kicking in', 'sharing needles', 'penis envy...', 'praying the white in me away', 'the miracle that is being born with a fat ass', "mom's hot, hot pockets", 'whipping it out in public', 'making a pouty face', "the kkk's lack of white privilege", 'wifely duties', 'a defective condom', 'that really hot fuckboy in my chemistry class', 'being an asian but also bad at math', 'natural selection', 'the fire emblem ', 'disney but kinda fruity', 'a lifetime of sadness, with a side of cake', 'parting the red sea', 'league of legends', 'a really, really, really big chicken', 'homoerotic volleyball montage', 'sports, but just a little sexually tense', 'flash flooding down there if you know what i mean', 'a really quick mating display', 'lots of poor life choices and luigi', 'testicular pain. and lots of it', 'my amazing sex life', 'all you can eat for only $4.99 baby', 'gloryholes but consensual', 'taking off my shirt instantly', 'deez nuts, baby', 'the goat that got more action than i ever could in one night ', 'nutting into a public pool', 'my "late" aunt sally', 'oversized lollipops', 'some very well-deserved me time', 'active self-loathing', 'putting my children on a leash', 'the little engine that really, really could', 'half-assed foreplay', 'one sword and a world of trouble', 'robin fire emblem', 'the invisible hand', 'really hot fantasies about gacha characters', "waiting 'til marriage to do the laundry", 'morgan freeman saying "yes. oh yes"', 'women eating yogurt seductively for a commercial', 'unfathomable stupidity', 'being a motherfucking sorcerer', 'leaving your mother a voicemail in the morning', 'genital piercings', 'my collection of really high-tech sex toys', 'an erection that would put my father to shame', 'balls', "that white kid's grandma", 'picking up girls at the right-wing hair salon', 'really fresh tentacles', "not reciprocating in oral sex because be shapiro said that's a liberal thing to do", 'too much white stuff', 'farting like a girlboss and walking away', 'being european', 'actually taking candy from a baby', 'something about being chinese', 'menstruation these days', 'the milk man', 'really powerful thighs', 'the gentle touch of a woman, aged 5', 'the sexinator 3000- v.1.1.69', 'hot bitches in my dms', 'that really cute republican', 'the true meaning of a white christmas', 'the homosexual agenda', 'suicidal ideation', 'hiding a boner in public', 'oompa loompa ', 'drinking alone at 4:20pm to feel something', 'my wife ', 'sexy penguin lingerie', 'pulling out', 'preteens and their hormones', "doin' it in the butt", 'panda enrichment and breeding center', 'tickling my scrotum because my wife left me', "firing a rifle to signal to everyone in a 20-foot radius i haven't been loved in years", "licking things to claim them as one's own", 'really, really, really hot grandmas', 'cuddling with my wife and her boyfriend', 'catboy enrichment center(s)', 'anime girls shoving their tits in my face', "a literal child going 'ara ara'", 'freeing me from this mortal coil ', "my mom's sandal", 'the overwatch servers crashing', 'world war 2 electric boogaloo', 'the spanish dickquisition', 'a college degree in this god-forsaken economy', 'hot dogs, but if they were french', "obama's sweet, sweet voice", "hannah montana's undiagnosed bipolar disorder", 'the love my mother never gave me because she was too busy with her real lovechild, netflix', 'thinking that cavemen peaked with the wheel and the fire', 'psychedelics and the inevitable fall of man', "because it's purble", 'sad cat memes', 'licking it off before the bugs get to it', "coding for hours in hopes of beating 2nd graders at coolmathgames.com's challenge levels", 'moving to florida', 'telling my husband i love him', 'my 88-year old father', 'that cute girl in the boxing ring looking my way']
    answers = cleanAnswers(rawAnswers)
    random.shuffle(answers)

    return answers
