import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['She', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'Their']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois',
          'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Apple', 'God', 'Man',
         'Beast', 'Coward', 'Loser', 'Mother', 'Teachers', 'Homelander']
PLACES = ['Space', 'Womb', 'Anal', 'House', 'Library', 'Ship',
          'Car', 'Jungle', 'Comic Shop', 'School', 'World', 'Dream']
WHEN = ['Soon', 'Tomorrow', 'Later this year', 'LIVE NOW', '100 years ago', 'next 20 minutes']



def main():
    while True:
        response = input("Enter number of clickbait headlines to generate: ")
        if not response.isdecimal():
            print("Enter a number.")
        else:
            numberOfHeadlines = int(response)
            break
    headlines = ""
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)
        if clickbaitType == 1:
            headlines = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headlines = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headlines = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headlines = generateYouWontBelievedHeadline()
        elif clickbaitType == 5:
            headlines = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headlines = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headlines = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headlines = generateJobAutomatedHeadline()
    # This prints each letter of the headlines instead.
    # for i in range(len(headlines)):
    #    print(f"{i}. {headlines[i]}")
        print(headlines)
    when = random.choice(WHEN)
    website = random.choice(['WEBSITE', 'BLOG', 'FACEBOOK', 'GOOGLES', 'FACEBOOK', 'TWITTER', 'INSTAGRAM'])
    print()
    print(f"Post these to our {website} {when} or you\'re fired!")


def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS).upper()
    return f"ARE MILLENNIALS KILLING {noun} INDUSTRY?"


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS).upper()
    pluralNoun = random.choice(NOUNS).upper() + 'S'
    when = random.choice(WHEN).upper()
    return f"WITHOUT THIS {noun}, {pluralNoun} COULD KILL YOU {when}"


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS).upper()
    state = random.choice(STATES).upper()
    noun1 = random.choice(NOUNS).upper()
    noun2 = random.choice(NOUNS).upper()
    return f"BIG COMPANIES HATE {pronoun}! SEE HOW THIS {state} {noun1} INVENTED A CHEAPER {noun2}"


def generateYouWontBelievedHeadline():
    state = random.choice(STATES).upper()
    noun = random.choice(NOUNS).upper()
    pronoun = random.choice(POSSESSIVE_PRONOUNS).upper()
    place = random.choice(PLACES).upper()
    return f"YOU WON\'T BELIEVE WHAT THIS {state} {noun} FOUND IN {pronoun} {place}"


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS).upper() + 'S'
    pluralNoun2 = random.choice(NOUNS).upper() + 'S'
    return f"WHAT {pluralNoun1} DONT\'T WANT YOU TO KNOW ABOUT {pluralNoun2}"


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS).upper()
    state = random.choice(STATES).upper()
    return f"{number} GIFT IDEAS TO GIVE YOUR {noun} FROM {state}"


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS).upper() + 'S'
    number2 = random.randint(1, number1)
    return (f"{number1} REASONS WHY {pluralNoun} ARE MORE INTERESTING THAN YOU THINK "
            f"(NUMBER {number2} WILL SURPRISE YOU!)")


def generateJobAutomatedHeadline():
    state = random.choice(STATES).upper()
    noun = random.choice(NOUNS).upper()

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i].upper()
    pronoun2 = PERSONAL_PRONOUNS[i].upper()
    if pronoun1 == "Their":
        return f"THIS {state} {noun} DID\'T THINK ROBOTS WOULD TAKE {pronoun1} JOB. {pronoun2} WERE WRONG."
    else:
        return f"THIS {state} {noun} DID\'T THINK ROBOTS WOULD TAKE {pronoun1} JOB. {pronoun2} WAS WRONG."


if __name__ == "__main__":
    main()

"""
1. NameError: name 'numberOfHeadlines' is not defined
2. TypeError: 'str' object cannot be interpreted as an integer
3. IndexError: Cannot choose from an empty sequence
"""