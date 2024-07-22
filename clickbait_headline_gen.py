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
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1,8)
        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelievedHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHealine()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAumatedHeadline()

        print(headline)
    print()
    website = random.choice()
    when = random.choice(WHEN).lower(['website', 'blag', 'Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram'])
    print(f"Post these to our {website} {when} or you\'re fired!")


if __name__ == "__main__":
    main()